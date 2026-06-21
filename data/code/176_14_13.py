import re

def find_letter_sequences(s):
    return set(re.findall(r'\b[a-zA-Z]+\b', s))

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет, мир!"
    print(find_letter_sequences(sample_string))