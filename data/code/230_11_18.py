def validate_input(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    for key, value in input_dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("All keys and values must be strings")

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