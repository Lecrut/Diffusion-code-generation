def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def capitalize_first_letter(s):
    validate_input(s)
    if len(s) == 0:
        return s
    first_char = s[0].upper()
    rest_of_string = s[1:]
    return first_char + rest_of_string

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "python", "", "a"]
    for value in sample_values:
        print(capitalize_first_letter(value))