def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    input_string = "hello world python"
    result = replace_spaces_with_underscores(input_string)
    print(result)