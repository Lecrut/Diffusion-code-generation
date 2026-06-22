import string
from collections import Counter

def find_repeated_characters(input_str):
    translator = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_string = input_str.translate(translator)
    char_counts = Counter(cleaned_string.lower())
    repeated_chars = sorted([char for char, count in char_counts.items() if count > 1])
    return repeated_chars

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test: AaBbCc... 112233!"
    result = find_repeated_characters(sample_text)
    print(result)