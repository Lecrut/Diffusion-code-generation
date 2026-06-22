class FrequencySorter:
    @staticmethod
    def sort_frequencies(freq_dict):
        sorted_keys = sorted(freq_dict.keys())
        sorted_dict = {key: freq_dict[key] for key in sorted_keys}
        return sorted_dict

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    sorter = FrequencySorter()
    sorted_freqs = sorter.sort_frequencies(sample_freqs)
    print(sorted_freqs)