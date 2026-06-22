def is_valid_string(s):
    return isinstance(s, str)

def capitalize_first_letter(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_string = "good evening"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)