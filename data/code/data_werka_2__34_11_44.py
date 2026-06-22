def capitalize_first_letter(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = ["hello", "world", "PYTHON", "123abc", "!@#"]
    for value in sample_values:
        print(capitalize_first_letter(value))