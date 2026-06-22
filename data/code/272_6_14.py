def sort_word_frequencies(freq_dict):
    sorted_keys = sorted(freq_dict.keys())
    sorted_dict = {key: freq_dict[key] for key in sorted_keys}
    return sorted_dict

if __name__ == '__main__':
    sample_freq_dict = {'banana': 3, 'apple': 4, 'cherry': 2}
    sorted_freq_dict = sort_word_frequencies(sample_freq_dict)
    print(sorted_freq_dict)