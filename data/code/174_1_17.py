class WordFrequencyCounter:
    @staticmethod
    def count_frequencies(words):
        frequency_dict = {}
        for word in words:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
        return frequency_dict

    @staticmethod
    def sort_by_frequency(frequency_dict):
        sorted_list = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
        return sorted_list

if __name__ == '__main__':
    sample_words = ["apple", "banana", "apple", "orange", "banana", "grape"]
    frequencies = WordFrequencyCounter.count_frequencies(sample_words)
    sorted_frequencies = WordFrequencyCounter.sort_by_frequency(frequencies)
    print(sorted_frequencies)