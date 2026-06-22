def parse_comma_separated(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    for item in input_string.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample_input = " apple, ,banana , cherry, ,date "
    result = list(parse_comma_separated(sample_input))
    print(result)