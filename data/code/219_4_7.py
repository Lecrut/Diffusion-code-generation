def find_max_value(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5}
    result = find_max_value(sample_dict)
    print(result)