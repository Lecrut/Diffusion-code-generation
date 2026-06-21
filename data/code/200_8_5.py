from collections import Counter

def count_words(words):
    return Counter(words)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_counts = count_words(sample_words)
    print(word_counts)