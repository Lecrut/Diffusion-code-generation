from collections import Counter

def count_word_occurrences(words_list):
    return Counter(words_list)

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    word_count = count_word_occurrences(sample_words)
    print(word_count)