import time
import pyautogui
import pyperclip


# Give yourself a couple of seconds to switch to the target application
time.sleep(2)

# Click the chrome icon
pyautogui.click(1231, 1055)
time.sleep(0.5)

# Drag to select
pyautogui.moveTo(670, 211, duration=0.2)
pyautogui.dragTo(1643, 987, duration=0.8, button="left")
time.sleep(0.3)

# Copy the selected content
pyautogui.hotkey("ctrl", "c")
pyautogui.click(1484 , 953)
time.sleep(0.5)  # Wait for clipboard to update

# Read clipboard into a variable
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)


