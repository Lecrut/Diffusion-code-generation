class WordFrequencySorter:
    @staticmethod
    def sort_frequencies(freq_dict):
        sorted_keys = sorted(freq_dict.keys())
        return {key: freq_dict[key] for key in sorted_keys}

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    sorter = WordFrequencySorter()
    sorted_freqs = sorter.sort_frequencies(sample_freqs)
    print(sorted_freqs)