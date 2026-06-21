from collections import Counter

def count_words(words_list):
    return Counter(words_list)

if __name__ == '__main__':
    sample_text = ["apple", "banana", "apple", "orange", "banana", "grape"]
    word_counts = count_words(sample_text)
    print(word_counts)