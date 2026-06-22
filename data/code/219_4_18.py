def find_max_value(dictionary):
    if not dictionary:
        return None, None
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 1, 'e': 5, 'f': 9, 'g': 2}
    key, value = find_max_value(sample_dict)
    print(f"Key: {key}, Value: {value}")