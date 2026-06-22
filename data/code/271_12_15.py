from collections import Counter
import re

def extract_words(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string.")
    return re.findall(r'\b\w+\b', text.lower())

def count_word_frequencies(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Words must be a list of strings.")
    return Counter(words)

def get_top_n_words(word_counts, n):
    if not isinstance(word_counts, Counter) or not isinstance(n, int) or n <= 0:
        raise ValueError("Word counts must be a Counter object and n must be a positive integer.")
    return word_counts.most_common(n)

def top_n_words(text, n):
    words = extract_words(text)
    word_counts = count_word_frequencies(words)
    return get_top_n_words(word_counts, n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone! Welcome to the world of Python."
    top_3_words = top_n_words(sample_text, 3)
    print(top_3_words)