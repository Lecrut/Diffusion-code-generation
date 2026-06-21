from collections import Counter

def count_word_occurrences(word_list):
    return Counter(word_list)

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    word_counts = count_word_occurrences(sample_words)
    print(word_counts)