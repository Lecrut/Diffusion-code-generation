def is_valid_string(s):
    return isinstance(s, str)

def capitalize_first_letter(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    if not s:
        return ""
    first_char = s[0].upper()
    rest_of_string = s[1:]
    return first_char + rest_of_string

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "HELLO WORLD",
        "hello WORLD",
        "hElLo WoRlD",
        "",
        "a",
        "123abc",
        "!@#abc"
    ]
    for value in sample_values:
        try:
            print(capitalize_first_letter(value))
        except ValueError as e:
            print(e)