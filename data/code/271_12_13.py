from collections import Counter
import re

def top_n_words(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Python is great. Python is versatile. Great tools for programming."
    top_3_words = top_n_words(sample_text, 3)
    print(top_3_words)