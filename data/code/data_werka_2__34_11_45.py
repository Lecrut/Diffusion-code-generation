def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s

def capitalize_first_letter(s):
    s = validate_input(s)
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "Python", "", "a", "123abc"]
    for value in sample_values:
        print(capitalize_first_letter(value))