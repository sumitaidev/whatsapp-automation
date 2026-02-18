import pywhatkit as w
import pyautogui
import keyboard as k
import time

def send_whatsapp_message(number, message, hour, minute):
    # Send WhatsApp message (tab_close=False to control manually)
    w.sendwhatmsg(number, message, hour, minute, tab_close=False)

    # Wait for WhatsApp Web to load
    time.sleep(5)

    # Click message box (adjust coordinates if needed)
    pyautogui.click(1050, 950)

    # Press Enter
    k.press_and_release('enter')

    return "Message Scheduled Successfully!"
