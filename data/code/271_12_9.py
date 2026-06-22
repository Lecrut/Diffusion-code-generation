from collections import Counter
import re

def validate_input(text, n):
    if not isinstance(text, str) or not isinstance(n, int):
        raise ValueError("Invalid input type. Text must be a string and n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())

def count_word_occurrences(words):
    return Counter(words)

def get_top_n_words(word_counts, n):
    return word_counts.most_common(n)

def top_n_words(text, n):
    validate_input(text, n)
    words = extract_words(text)
    word_counts = count_word_occurrences(words)
    return get_top_n_words(word_counts, n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone! Welcome to the world of Python."
    top_3_words = top_n_words(sample_text, 3)
    print(top_3_words)