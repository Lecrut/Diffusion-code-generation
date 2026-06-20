SPACE_CHAR = ' '
UNDERSCORE_CHAR = '_'

def _validate_input(input_text):
    if not isinstance(input_text, str):
        raise TypeError("Expected a string input")
    return True

def convert_spaces_to_underscores(text):
    _validate_input(text)
    result = []
    for char in text:
        if char == SPACE_CHAR:
            result.append(UNDERSCORE_CHAR)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "convert spaces to underscores here"
    output = convert_spaces_to_underscores(sample_string)
    print(output)