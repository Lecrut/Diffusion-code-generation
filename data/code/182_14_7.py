def string_to_char_list(input_string: str) -> list:
    return [char for char in input_string]

if __name__ == '__main__':
    sample_input = "hello"
    result = string_to_char_list(sample_input)
    print(result)