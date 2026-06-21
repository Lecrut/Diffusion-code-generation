from collections import Counter

class WordCounter:
    @staticmethod
    def count_words(words):
        return Counter(words)

if __name__ == '__main__':
    sample_text = "hello world hello python programming"
    word_counts = WordCounter.count_words(sample_text.split())
    print(word_counts)