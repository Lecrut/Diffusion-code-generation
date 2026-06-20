def split_and_trim(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    parts = input_string.split(',')
    trimmed_parts = [part.strip() for part in parts]
    non_empty_parts = [part for part in trimmed_parts if part]
    return non_empty_parts

if __name__ == '__main__':
    sample_input = "apple, banana, , cherry,  grape , orange,"
    result = split_and_trim(sample_input)
    print(result)