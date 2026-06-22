from collections import Counter
import re

def top_n_words(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count.most_common(n)

if __name__ == '__main__':
    sample_text = "Hello world hello Python. Hello everyone!"
    n = 3
    print(top_n_words(sample_text, n))