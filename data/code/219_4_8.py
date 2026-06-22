def find_max_value(dictionary):
    return max(dictionary, key=dictionary.get), dictionary[max(dictionary, key=dictionary.get)]

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 1, 'e': 5, 'f': 9, 'g': 2}
    max_key, max_value = find_max_value(sample_dict)
    print(f"Key: {max_key}, Value: {max_value}")