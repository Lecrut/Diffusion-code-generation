class WordFrequencyCounter:
    WORDS = ["apple", "banana", "apple", "orange", "banana", "grape"]

    @staticmethod
    def count_frequencies(words):
        freq_dict = {}
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = WordFrequencyCounter()
    frequencies = counter.count_frequencies(WordFrequencyCounter.WORDS)
    print(frequencies)