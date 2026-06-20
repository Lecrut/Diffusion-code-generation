def convert_spaces_to_underscores(text: str) -> str:
    return text.replace(" ", "_")

if __name__ == '__main__':
    input_string = "hello world this is a test"
    result = convert_spaces_to_underscores(input_string)
    print(result)