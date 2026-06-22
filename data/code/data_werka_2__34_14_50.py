def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    
    stripped_s = s.strip()
    if not stripped_s:
        return s
    
    first_char = stripped_s[0].upper()
    remaining_chars = stripped_s[1:]
    capitalized_str = first_char + remaining_chars
    
    leading_spaces = len(s) - len(stripped_s)
    trailing_spaces = len(s) - len(stripped_s) - leading_spaces
    
    return ' ' * leading_spaces + capitalized_str + ' ' * trailing_spaces

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "  hello world  ",
        "",
        "hELLO",
        "123abc",
        "   ",
        "a",
        "multiple   spaces"
    ]
    for value in sample_values:
        print(capitalize_first_letter(value))