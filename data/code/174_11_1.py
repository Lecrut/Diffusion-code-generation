import collections
def count_string_frequencies(string_list):
    frequency_map = {}
    for s in string_list:
        frequency_map[s] = frequency_map.get(s, 0) + 1
    return frequency_map
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_string_frequencies(sample_list)
    print(result)