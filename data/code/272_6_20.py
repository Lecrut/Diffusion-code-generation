class WordFrequencySorter:
    def __init__(self, freq_dict):
        self.freq_dict = freq_dict

    def sort_frequencies(self):
        sorted_keys = sorted(self.freq_dict.keys())
        return {key: self.freq_dict[key] for key in sorted_keys}

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    sorter = WordFrequencySorter(sample_freqs)
    sorted_freqs = sorter.sort_frequencies()
    print(sorted_freqs)