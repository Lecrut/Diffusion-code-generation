import re

def find_letter_sequences(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, world! 123 Python 3.8 is fun."
    print(find_letter_sequences(sample_text))