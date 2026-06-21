import re

def extract_letter_sequences(text):
    sequences = re.findall(r'\b[a-zA-Z]+\b', text)
    return sequences

if __name__ == '__main__':
    sample_text = "Hello, World! 123 Python 3.8 and another sentence."
    letter_sequences = extract_letter_sequences(sample_text)
    print(letter_sequences)