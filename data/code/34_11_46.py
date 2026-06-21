def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        return s
    first_char = s[0].upper()
    rest_of_string = s[1:]
    capitalized_string = first_char + rest_of_string
    return capitalized_string

if __name__ == '__main__':
    sample_values = ["example", "TEST", "another", "", "b"]
    for value in sample_values:
        print(capitalize_first_letter(value))