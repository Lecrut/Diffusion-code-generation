from collections import Counter
import re

def count_top_words(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Hello world. Hello everyone. Welcome to the world of Python."
    top_n_words = count_top_words(sample_text, 3)
    print(top_n_words)