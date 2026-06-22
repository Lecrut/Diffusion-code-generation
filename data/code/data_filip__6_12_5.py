SPACE_CHAR = ' '
UNDERSCORE_CHAR = '_'

def convert_spaces_to_underscores(source_text):
    if not isinstance(source_text, str):
        raise TypeError("Input must be a string")
    if SPACE_CHAR not in source_text:
        return source_text
    return source_text.replace(SPACE_CHAR, UNDERSCORE_CHAR)

if __name__ == '__main__':
    predefined_value = "The quick brown fox jumps over the lazy dog"
    transformed_value = convert_spaces_to_underscores(predefined_value)
    print(transformed_value)