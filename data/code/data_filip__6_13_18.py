def replace_spaces_with_underscores(constant_string: str) -> str:
    return constant_string.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world python"
    result = replace_spaces_with_underscores(sample_input)
    print(result)