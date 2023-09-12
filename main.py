import pyautogui
import pytesseract
import keyboard
import time
import re
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def calculate_answer(expression):
    try:
        answer = eval(expression)  # Используем функцию eval() для вычисления значения выражения
        return answer
    except:
        return "Некорректное выражение"

def process_string(input_string):
    two_digit_numbers = re.findall(r'\b\d{2}\b', input_string)
    
    for number in two_digit_numbers:
        input_string = input_string.replace(number, number[0])
    
    return input_string

def replace_fives_with_threes(input_string):
    output_string = input_string.replace("5", "3")
    return output_string

def replace_four_with_plus(input_string):
    output_string = input_string.replace("4", "+")
    return output_string

def convert_to_grayscale(image):
    return image.convert("L")

def get_text(screenshot):
    grayscale_screenshot = convert_to_grayscale(screenshot)
    return pytesseract.image_to_string(grayscale_screenshot)

def click(X, Y):
    pyautogui.click(x=X, y=Y, duration=0.3)

while True:
    screenshot = pyautogui.screenshot(region=(704, 577, 502, 83))
    if keyboard.is_pressed('`'):
        break
    primer = get_text(screenshot)[:-3]
    prim = process_string(primer)
    prim = process_string(primer)
    prim = replace_fives_with_threes(prim)
    prim = replace_four_with_plus(prim)
    print(prim)
    answ = calculate_answer(prim)
    print(answ)
    if answ == 1:
        click(962, 690)
    elif answ == 2:
        click(963, 760)
    elif answ == 3:
        click(965, 831)
    time.sleep(1.4)

