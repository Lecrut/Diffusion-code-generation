from collections import Counter

class WordCounter:
    @staticmethod
    def count_words(word_list):
        return Counter(word_list)

if __name__ == '__main__':
    sample_text = "hello world hello python world"
    words = sample_text.split()
    word_count = WordCounter.count_words(words)
    print(word_count)