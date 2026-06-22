class WordFrequencySorter:
    def __init__(self):
        self.freq_dict = {}

    def add_word(self, word, frequency):
        if word in self.freq_dict:
            self.freq_dict[word] += frequency
        else:
            self.freq_dict[word] = frequency

    def sort_words(self):
        sorted_keys = sorted(self.freq_dict.keys())
        return {key: self.freq_dict[key] for key in sorted_keys}

if __name__ == '__main__':
    sorter = WordFrequencySorter()
    sorter.add_word('zebra', 5)
    sorter.add_word('apple', 3)
    sorter.add_word('banana', 1)
    sorter.add_word('cherry', 2)
    
    sorted_freqs = sorter.sort_words()
    print(sorted_freqs)