def sort_word_frequencies(freq_dict):
    sorted_keys = sorted(freq_dict.keys())
    return {key: freq_dict[key] for key in sorted_keys}

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    if not all(isinstance(key, str) and isinstance(value, int) for key, value in sample_freqs.items()):
        raise ValueError("Invalid frequency dictionary. Keys must be strings and values must be integers.")
    
    sorted_freqs = sort_word_frequencies(sample_freqs)
    print(sorted_freqs)