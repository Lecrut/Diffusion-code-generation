def validate_input(input_list):
    if not all(isinstance(item, str) for item in input_list):
        raise ValueError("All elements in the list must be strings")

def map_to_uppercase(strings):
    return list(map(lambda s: s.upper(), strings))

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    validate_input(sample_strings)
    uppercased_strings = map_to_uppercase(sample_strings)
    print(uppercased_strings)