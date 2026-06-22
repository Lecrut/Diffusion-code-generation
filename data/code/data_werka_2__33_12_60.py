def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    words = input_string.split()
    result = ''.join(words)
    return result

if __name__ == '__main__':
    test_input = "  Hello   world! \t This is another test. \n Let's see how it works. "
    try:
        output = remove_whitespace(test_input)
        print(output)
    except ValueError as e:
        print(e)