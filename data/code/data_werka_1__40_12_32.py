def get_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[0] if s else ''

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python"]
    for value in sample_values:
        try:
            print(get_first_letter(value))
        except ValueError as e:
            print(e)