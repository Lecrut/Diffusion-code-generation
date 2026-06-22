SAMPLE_INPUT = "convert these spaces to underscores"

def validate_string_input(value):
    if not isinstance(value, str):
        raise TypeError("Expected a string type")
    return True

def spaces_to_underscores(text):
    validate_string_input(text)
    result = text.replace(' ', '_')
    return result

if __name__ == '__main__':
    output = spaces_to_underscores(SAMPLE_INPUT)
    print(output)