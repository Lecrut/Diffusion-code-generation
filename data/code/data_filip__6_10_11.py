def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = replace_spaces_with_underscores(sample_string)
    print(result)