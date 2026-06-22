import re
from collections import Counter

def top_n_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(n)

if __name__ == '__main__':
    top_words = top_n_words('sample.txt', 5)
    print(top_words)