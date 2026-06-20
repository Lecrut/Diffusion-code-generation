def replace_whitespace_with_underscore(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World 123"
    result = replace_whitespace_with_underscore(sample_input)
    print(result)