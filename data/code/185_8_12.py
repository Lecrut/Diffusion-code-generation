import re

def is_numeric(word):
    return word.replace('.', '', 1).isdigit()

def extract_numbers(text):
    words = text.split()
    numbers = [float(word) for word in words if is_numeric(word)]
    return numbers

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(extract_numbers(sample_text))