def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[0].upper() + s[1:] if s else ''

if __name__ == '__main__':
    sample_string = "hello world"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)