import random
import time
import tkinter as tk
import pyttsx3
import os 

warnings = [
    "Dear Viral, it's time to prioritize your health. Please take a short break.",
    "Your well-being matters. It's time for a brief rest.",
    "Hi Viral,Please Remember, a short break can boost your productivity and health.",
    "Taking breaks enhances your work quality. Take a moment to relax.",
    "It's been an hour of hard work. Time to unwind for a while.",
    "Dear Viral,Your eyes and body need a break. Pause and relax for a moment.",
    "A short break can improve your focus. Please take some time off.",
    "Prioritize your health. A brief break is beneficial. Please rest."
]

shutdown_threshold = warnings.__len__()  # Set the shutdown threshold to the number of warnings

warning_count = 0  # Initialize the warning count

def display_break_reminder():
    global warning_count  # Use the global warning_count variable

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.configure(bg='light blue')   
    
    reminder_label = tk.Label(
        root,
        text="Sir, please take a break!\nStretch, relax, and rest your eyes for 10 minutes.",
        font=("Helvetica", 24),   
        bg='light blue',
    )
    reminder_label.pack(expand=True, fill=tk.BOTH)

    # Voice notification
    engine = pyttsx3.init()
    engine.say("Sir, please take a break!")
    engine.runAndWait()

    warning_count_label = tk.Label(
        root,
        text=f"Warnings: {warning_count}/{shutdown_threshold}",
        font=("Helvetica", 16),
        bg='light blue',
    )
    warning_count_label.pack(expand=True, fill=tk.BOTH)

    def on_click(event):
        global warning_count  # Use the global warning_count variable
        choice = random.choice(warnings)  # Randomly select a warning message
        info_label = tk.Label(
            root,
            text=choice,
            font=("Helvetica", 16),
            bg='light blue',
        )
        engine.say(choice)  # Speak the random warning
        engine.runAndWait()
        info_label.pack(expand=True, fill=tk.BOTH)

        warning_count += 1  # Increment the warning count

        if warning_count >= shutdown_threshold:
            # If warning count exceeds the threshold, notify and shutdown
            notify_shutdown_label = tk.Label(
                root,
                text=f"Warning count reached {shutdown_threshold}. PC will shut down.",
                font=("Helvetica", 16),
                bg='light blue',
            )
            notify_shutdown_label.pack(expand=True, fill=tk.BOTH)
            engine.say(f"Warning count reached {shutdown_threshold}. PC will shut down.")
            os.system("shutdown /s /t 1")
            engine.runAndWait()
            root.after(5000, root.destroy)  # Close the window after 5 seconds and proceed with shutdown
        else:
            warning_count_label.config(text=f"Warnings: {warning_count}/{shutdown_threshold}")  # Update the warning count label
            root.after(10000, root.destroy)  # Close the window after 10 seconds if not shutting down
    
    root.bind("<Button-1>", on_click)
    
    root.mainloop()

print("Timer started...")
print("Take a break reminder every one hour.")

while True:
    # time.sleep(3600)  # Sleep for 1 hour
    display_break_reminder()
