import re

def extract_numbers(text):
    return [float(num) for num in re.findall(r'-?\d+\.\d+|\d+', text)]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(extract_numbers(sample_text))