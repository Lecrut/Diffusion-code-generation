from collections import Counter

def count_words(word_list):
    return Counter(word_list)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    word_count = count_words(sample_words)
    print(word_count)