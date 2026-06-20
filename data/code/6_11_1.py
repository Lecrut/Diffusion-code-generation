def convert_spaces_to_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world example code"
    result = convert_spaces_to_underscores(sample_input)
    print(result)