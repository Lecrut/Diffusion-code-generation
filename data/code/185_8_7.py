import re

def is_numeric(word):
    return word.replace('.', '', 1).isdigit()

def extract_numbers(text):
    words = text.split()
    numeric_words = [word for word in words if is_numeric(word)]
    return [float(num) for num in numeric_words]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(extract_numbers(sample_text))