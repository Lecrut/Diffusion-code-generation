def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World"
    result = replace_spaces_with_underscores(sample_input)
    print(result)