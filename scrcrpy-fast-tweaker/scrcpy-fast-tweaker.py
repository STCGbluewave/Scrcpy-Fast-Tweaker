# Code by me & Copilot (Copilot helped fix errors and gave suggestions)

import subprocess
import os

# Define Scrcpy command
scrcpy_cmd = "scrcpy"

print("Welcome to scrcpy-fast-tweaker!")
# Ask user if they want to change aspect ratio
aspect_ratio = input("What do you want the aspect ratio to be? (1080p) Options: '16:9' (default), '4:3', 'Keep' ").strip().lower() or "16:9"

if aspect_ratio == "16:9":
    os.system("adb shell wm size 1080x1920")
elif aspect_ratio == "4:3":
    os.system("adb shell wm size 1080x1440")
elif aspect_ratio == "keep":
    os.system("adb shell wm size reset")
else:
    print("Invalid input! Keeping default aspect ratio.")


# User input for fullscreen mode
fullscreen = input("Should it be Fullscreen? Yes or No? ").strip().lower()
if fullscreen == "yes":
    scrcpy_cmd += " -f"

# User input for FPS setting
fps = input("Enter max FPS (default: 60): ").strip() or "60"
scrcpy_cmd += f" --max-fps={fps}"

# User input for video quality
bitrate = input("Enter video bitrate (default: 8M): ").strip() or "8M"
scrcpy_cmd += f" --video-bit-rate={bitrate}"

# User input for recording
recording = input("Do you want to record gameplay? Yes or No? ").strip().lower()
if recording == "yes":
    filename = input("Enter filename (default: session): ").strip() or "session"
    scrcpy_cmd += f" -r {filename}.mp4"
    
# Ask user to turn off the screen
screen_off = input("Turn phone screen off? Yes or No? (default: yes) ").strip().lower() or "yes"
if screen_off == "yes":
    scrcpy_cmd += " --turn-screen-off"

# Run Scrcpy inside the same terminal with keyboard & mouse support
subprocess.run(f"{scrcpy_cmd} --keyboard uhid --mouse uhid".split())

# Restore screen resolution after Scrcpy exits
os.system("adb shell wm size reset")

print("Done! Goodbye. 😃")