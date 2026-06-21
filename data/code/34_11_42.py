def capitalize_first_letter(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    if len(input_string) == 0:
        return input_string
    return input_string[0].upper() + input_string[1:]

if __name__ == '__main__':
    sample_values = ["hello world", "PYTHON", "123abc", "", "single"]
    for value in sample_values:
        print(capitalize_first_letter(value))