def find_min_max(dictionary):
    if not isinstance(dictionary, dict) or not all(isinstance(v, (int, float)) for v in dictionary.values()):
        raise ValueError("Input must be a dictionary with numeric values.")
    
    min_key = min(dictionary, key=dictionary.get)
    max_key = max(dictionary, key=dictionary.get)
    
    return (min_key, dictionary[min_key]), (max_key, dictionary[max_key])

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    min_value, max_value = find_min_max(sample_dict)
    print(min_value, max_value)