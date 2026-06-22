def split_by_comma(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    parts = input_string.split(',')
    return [part.strip() for part in parts if part.strip()]

if __name__ == '__main__':
    sample_input = " apple , banana , , cherry ,  date  "
    result = split_by_comma(sample_input)
    print(result)