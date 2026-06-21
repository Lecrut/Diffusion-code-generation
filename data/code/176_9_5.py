import re

def extract_letter_sequences(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return words

if __name__ == '__main__':
    sample_text = "Python 3.8 is awesome! #1"
    letter_sequences = extract_letter_sequences(sample_text)
    print(letter_sequences)