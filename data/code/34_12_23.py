def capitalize_first_letter(input_string):
    if not input_string:
        return ""
    return input_string[0].upper() + input_string[1:]

if __name__ == '__main__':
    sample_values = ["hello world", "PYTHON", "123abc", "", "a"]
    for value in sample_values:
        print(capitalize_first_letter(value))