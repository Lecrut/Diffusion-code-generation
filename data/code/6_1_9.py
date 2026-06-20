SPACE_CHAR = ' '
UNDERSCORE_CHAR = '_'

def transform_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Expected string input")
    parts = text.split(SPACE_CHAR)
    return UNDERSCORE_CHAR.join(parts)

if __name__ == '__main__':
    sample_value = "The quick brown fox"
    output = transform_spaces(sample_value)
    print(output)