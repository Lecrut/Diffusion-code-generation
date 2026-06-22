def validate_input(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")

def print_uppercase_pairs(dictionary):
    validate_input(dictionary)
    for key, value in dictionary.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    print_uppercase_pairs(sample_dict)