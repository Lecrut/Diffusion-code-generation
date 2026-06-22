import re
from collections import Counter

def find_repeated_characters(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    counts = Counter(cleaned_text)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_input = "Hello, World! 123 222!!"
    result = find_repeated_characters(sample_input)
    print(result)