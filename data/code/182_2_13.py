def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def string_to_char_list(s):
    validate_input(s)
    return list(s)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    char_list = string_to_char_list(sample_string)
    print(char_list)