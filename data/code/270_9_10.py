def remove_spaces(input_string):
    NO_SPACE = ' '
    result = ''
    for char in input_string:
        if char != NO_SPACE:
            result += char
    return result

if __name__ == '__main__':
    SAMPLE_INPUT = "Hello World"
    print(remove_spaces(SAMPLE_INPUT))