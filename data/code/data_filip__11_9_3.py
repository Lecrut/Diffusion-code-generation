import string
import collections

def find_repeated_characters(input_string):
    cleaned = input_string.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    char_counts = collections.Counter(cleaned.lower())
    repeated = [char for char, count in char_counts.items() if count > 1]
    return sorted(repeated)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    result = find_repeated_characters(sample_text)
    print(result)