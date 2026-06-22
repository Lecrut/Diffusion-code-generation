class WordFrequencyAnalyzer:
    @staticmethod
    def most_frequent_word(text):
        words = text.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return max(word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    sample_text = "hello world hello python programming is fun and exciting"
    most_frequent, count = WordFrequencyAnalyzer.most_frequent_word(sample_text)
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")