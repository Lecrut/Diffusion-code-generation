def is_valid_string(s):
    return isinstance(s, str)

def capitalize_first_letter(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    if not s:
        return s
    first_char = s[0].upper()
    remaining_chars = s[1:]
    return first_char + remaining_chars

if __name__ == '__main__':
    sample_string = "good afternoon"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)