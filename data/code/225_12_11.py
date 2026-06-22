def find_min_max(dictionary):
    min_key = min(dictionary, key=dictionary.get)
    max_key = max(dictionary, key=dictionary.get)
    return (min_key, dictionary[min_key]), (max_key, dictionary[max_key])

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    min_val, max_val = find_min_max(sample_dict)
    print(min_val, max_val)