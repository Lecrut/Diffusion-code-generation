def print_uppercase_pairs(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError("Input must be a dictionary")
    
    for key, value in dictionary.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Dictionary keys and values must be strings")
        
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {
        'apple': 'red',
        'banana': 'yellow',
        'cherry': 'red'
    }
    print_uppercase_pairs(sample_dict)