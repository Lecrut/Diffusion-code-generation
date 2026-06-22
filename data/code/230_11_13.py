def print_uppercase_pairs(dictionary):
    if not isinstance(dictionary, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in dictionary.items()):
        raise ValueError("Input must be a dictionary with string keys and values")
    
    for key, value in dictionary.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {
        'apple': 'red',
        'banana': 'yellow',
        'cherry': 'red'
    }
    print_uppercase_pairs(sample_dict)