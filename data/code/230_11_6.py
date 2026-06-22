def validate_input(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError("Input must be a dictionary")
    for key, value in dictionary.items():
        if not (isinstance(key, str) and isinstance(value, str)):
            raise ValueError("Dictionary keys and values must be strings")

def print_uppercase_pairs(dictionary):
    validate_input(dictionary)
    for key, value in dictionary.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {
        'apple': 'red',
        'banana': 'yellow',
        'cherry': 'red'
    }
    print_uppercase_pairs(sample_dict)