def replace_spaces_with_underscores(input_text: str) -> str:
    if not input_text:
        return input_text
    parts = input_text.split(' ')
    return '_'.join(parts)

if __name__ == '__main__':
    raw_data = "python programming language"
    transformed = replace_spaces_with_underscores(raw_data)
    print(transformed)