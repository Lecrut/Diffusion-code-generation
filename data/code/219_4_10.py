def find_max_value(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 1}
    result = find_max_value(sample_dict)
    print(result)