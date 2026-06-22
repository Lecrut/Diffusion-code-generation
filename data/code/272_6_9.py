def validate_input(freq_dict):
    if not isinstance(freq_dict, dict):
        raise ValueError("Input must be a dictionary.")
    for key, value in freq_dict.items():
        if not isinstance(key, str) or not isinstance(value, int):
            raise ValueError("Dictionary keys must be strings and values must be integers.")

def sort_word_frequencies(freq_dict):
    validate_input(freq_dict)
    sorted_keys = sorted(freq_dict.keys())
    sorted_dict = {key: freq_dict[key] for key in sorted_keys}
    return sorted_dict

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    sorted_freqs = sort_word_frequencies(sample_freqs)
    print(sorted_freqs)