from collections import Counter

def count_word_occurrences(words):
    return dict(Counter(words))

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_counts = count_word_occurrences(sample_words)
    print(word_counts)