from collections import Counter

def count_words(words):
    return Counter(words)

if __name__ == '__main__':
    sample_text = "hello world hello python world"
    word_counts = count_words(sample_text.split())
    print(word_counts)