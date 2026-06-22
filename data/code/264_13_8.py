import re
from collections import Counter

def find_most_frequent_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)
    return most_common[0] if most_common else ('', 0)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone. Welcome to the world of Python."
    print(find_most_frequent_word(sample_text))