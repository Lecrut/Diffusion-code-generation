def split_comma_delimited(input_string):
    return [s.strip() for s in input_string.split(',') if s.strip()]

if __name__ == '__main__':
    sample_input = "  apple , banana,,  cherry , ,date "
    result = split_comma_delimited(sample_input)
    print(result)