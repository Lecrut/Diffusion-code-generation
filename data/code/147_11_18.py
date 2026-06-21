def validate_input(input_list):
    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("Input must be a list of strings")

def sort_alphabetically(strings):
    validate_input(strings)
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date']
    print(sort_alphabetically(sample_strings))