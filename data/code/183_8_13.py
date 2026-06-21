def split_names_by_and(input_string):
    if not isinstance(input_string, str) or 'and' not in input_string:
        raise ValueError("Input must be a string containing the word 'and'")
    
    names = [name.strip() for name in input_string.split(' and ')]
    return names

if __name__ == '__main__':
    sample_input = "Alice and Bob and Charlie"
    print(split_names_by_and(sample_input))