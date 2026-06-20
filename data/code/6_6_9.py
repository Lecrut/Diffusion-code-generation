def convert_spaces_to_underscores(text: str) -> str:
    result = []
    for char in text:
        if char == ' ':
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello World This is a test"
    output_value = convert_spaces_to_underscores(sample_input)
    print(output_value)
    another_input = "No_spaces_here"
    print(convert_spaces_to_underscores(another_input))
    empty_input = ""
    print(convert_spaces_to_underscores(empty_input))
    multiple_spaces = "  Double   spaces  here "
    print(convert_spaces_to_underscores(multiple_spaces))