import re

NUMERIC_PATTERN = r'-?\d+\.\d+|\d+'

def extract_numbers(text):
    return [float(num) for num in re.findall(NUMERIC_PATTERN, text)]

if __name__ == '__main__':
    sample_text = "The temperature is 23.5 degrees, and the pressure is 101.3."
    print(extract_numbers(sample_text))