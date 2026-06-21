import re

def find_letter_sequences(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, World! 123 Python 3.8"
    letter_sequences = find_letter_sequences(sample_text)
    print(letter_sequences)