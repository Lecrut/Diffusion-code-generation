import re

def find_letter_sequences(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_text = "Hello, World! 123 ABC def."
    print(find_letter_sequences(sample_text))