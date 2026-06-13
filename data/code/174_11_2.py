def count_string_frequencies(list_of_strings):
    frequency_map = {}
    for s in list_of_strings:
        if s in frequency_map:
            frequency_map[s] += 1
        else:
            frequency_map[s] = 1
    return frequency_map
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_string_frequencies(sample_list)
    print(result)