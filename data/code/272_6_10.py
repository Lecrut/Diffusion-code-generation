def sort_word_frequencies(freq_dict):
    sorted_keys = sorted(freq_dict.keys())
    sorted_dict = {key: freq_dict[key] for key in sorted_keys}
    return sorted_dict

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
    sorted_freqs = sort_word_frequencies(sample_freqs)
    print(sorted_freqs)