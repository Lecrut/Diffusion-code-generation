def capitalize_initial(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s:
        return s
    first_char = s[0].upper()
    rest_of_string = s[1:]
    return first_char + rest_of_string

if __name__ == '__main__':
    sample_input = "python programming"
    result = capitalize_initial(sample_input)
    print(result)