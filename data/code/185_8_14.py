import re

def extract_numbers(text):
    try:
        return [float(num) for num in re.findall(r'-?\d+\.\d+|\b\d+', text)]
    except TypeError as e:
        raise ValueError("Invalid input: text must be a string") from e

if __name__ == '__main__':
    sample_text = "The temperature is 23.5 degrees, and the pressure is 101.3."
    print(extract_numbers(sample_text))