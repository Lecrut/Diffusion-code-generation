import collections

class WordCounter:
    TOP_N = 5

    @staticmethod
    def count_words(text):
        words = text.split()
        word_counts = collections.Counter(words)
        return word_counts.most_common(WordCounter.TOP_N)

if __name__ == '__main__':
    sample_string = "This is an example sentence for word counting optimization. This sentence contains some repeated words."
    result = WordCounter.count_words(sample_string)
    print(result)