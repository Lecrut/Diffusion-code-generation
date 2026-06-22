def find_max_value(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 7, 'c': 2, 'd': 9}
    print(find_max_value(sample_dict))