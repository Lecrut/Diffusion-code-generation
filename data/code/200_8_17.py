from collections import Counter

class WordCounter:
    @staticmethod
    def count_words(word_list):
        return dict(Counter(word_list))

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana apple"
    words = sample_text.split()
    word_counts = WordCounter.count_words(words)
    print(word_counts)