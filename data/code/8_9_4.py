def split_trimmed_commas(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    parts = input_string.split(',')
    result = [part.strip() for part in parts if part.strip()]
    return result

if __name__ == '__main__':
    sample_input = "  apple ,  banana, ,  cherry , ,date "
    result = split_trimmed_commas(sample_input)
    print(result)