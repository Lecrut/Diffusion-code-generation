from collections import Counter
import re

def top_n_words(text, n):
    if not isinstance(text, str) or not isinstance(n, int):
        raise ValueError("Text must be a string and n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone! Welcome to the world of Python."
    try:
        top_3_words = top_n_words(sample_text, 3)
        print(top_3_words)
    except ValueError as e:
        print(e)