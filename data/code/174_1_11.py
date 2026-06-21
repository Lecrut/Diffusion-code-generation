class WordFrequencyCounter:
    @staticmethod
    def count_words(words):
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency

    @staticmethod
    def sort_frequency(frequency):
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return sorted_frequency

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    word_count = WordFrequencyCounter.count_words(sample_words)
    sorted_word_count = WordFrequencyCounter.sort_frequency(word_count)
    print(sorted_word_count)