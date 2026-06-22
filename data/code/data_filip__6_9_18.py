def replace_spaces_with_underscores(text: str) -> str:
    separator = '_'
    return separator.join(text.split(' '))

if __name__ == '__main__':
    original_string = "a b c d e"
    transformed_string = replace_spaces_with_underscores(original_string)
    print(transformed_string)