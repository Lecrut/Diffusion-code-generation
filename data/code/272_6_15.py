def sort_word_frequencies(freq_dict):
    if not isinstance(freq_dict, dict) or any(not isinstance(k, str) or not isinstance(v, int) for k, v in freq_dict.items()):
        raise ValueError("Input must be a dictionary with string keys and integer values.")
    
    sorted_keys = sorted(freq_dict.keys())
    sorted_dict = {key: freq_dict[key] for key in sorted_keys}
    return sorted_dict

if __name__ == '__main__':
    sample_freqs = {'zebra': 5, 'apple': 3, 'banana': 1, 'cherry': 2}
    try:
        sorted_freqs = sort_word_frequencies(sample_freqs)
        print(sorted_freqs)
    except ValueError as e:
        print(e)