def is_non_empty_string(s):
    return isinstance(s, str) and len(s.strip()) > 0

def capitalize_first_letter(s):
    if not is_non_empty_string(s):
        return s
    stripped_s = s.strip()
    capitalized_s = stripped_s[0].upper() + stripped_s[1:]
    leading_spaces = len(s) - len(stripped_s)
    trailing_spaces = len(s) - len(stripped_s) - leading_spaces
    return ' ' * leading_spaces + capitalized_s + ' ' * trailing_spaces

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "  python programming  ",
        "",
        "hELLO",
        "123abc",
        "   ",
        "a",
        "multiple   spaces"
    ]
    for value in sample_values:
        print(capitalize_first_letter(value))