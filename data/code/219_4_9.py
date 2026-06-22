def find_max_value(dictionary):
    if not isinstance(dictionary, dict) or not dictionary:
        raise ValueError("Input must be a non-empty dictionary")
    
    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5}
    print("Max value in the dictionary:", find_max_value(sample_dict))