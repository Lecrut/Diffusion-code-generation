def split_names(input_string):
    if not isinstance(input_string, str) or '\t' not in input_string:
        raise ValueError("Input must be a string containing tab-separated names.")
    
    return [name.strip() for name in input_string.split('\t') if name.strip()]

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie\tDavid"
    try:
        result = split_names(sample_input)
        print(result)
    except ValueError as e:
        print(e)