def replace_whitespace_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World Example"
    result = replace_whitespace_with_underscores(sample_input)
    print(result)