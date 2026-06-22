def capitalize_first_letter(s):
    def is_valid_string(input_str):
        return isinstance(input_str, str)
    
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    
    if not s:
        return s
    
    first_char = s[0].upper()
    remaining_chars = s[1:]
    return first_char + remaining_chars

if __name__ == '__main__':
    sample_string = "welcome to the jungle"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)