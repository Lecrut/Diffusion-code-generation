from collections import Counter
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def top_n_words(word_counts, n):
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "Python programming is fun. Fun with Python programming!"
    word_counts = count_words(sample_text)
    top_3_words = top_n_words(word_counts, 3)
    print(top_3_words)