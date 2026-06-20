def split_comma_separated(input_string):
    if not input_string:
        return []
    parts = input_string.split(',')
    result = [part.strip() for part in parts if part.strip()]
    return result

if __name__ == '__main__':
    test_input = "apple, banana, , cherry ,date,"
    output = split_comma_separated(test_input)
    print(output)