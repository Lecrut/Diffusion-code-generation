class WordFrequencySorter:
    def __init__(self, freq_dict):
        self.freq_dict = freq_dict

    def sort_keys(self):
        return sorted(self.freq_dict.keys())

    def create_sorted_dict(self):
        sorted_keys = self.sort_keys()
        return {key: self.freq_dict[key] for key in sorted_keys}

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    sorter = WordFrequencySorter(sample_freqs)
    sorted_freqs = sorter.create_sorted_dict()
    print(sorted_freqs)