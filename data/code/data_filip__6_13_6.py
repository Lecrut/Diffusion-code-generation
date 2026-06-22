def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    input_string = "hello world python"
    result = replace_spaces_with_underscores(input_string)
    print(result)