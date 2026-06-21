def get_first_letter(s):
    if not s:
        raise ValueError("Input string cannot be empty")
    return s[0]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    first_letter = get_first_letter(sample_string)
    print(first_letter)