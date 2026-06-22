def get_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s:
        raise ValueError("Input string cannot be empty")
    return s[0]

if __name__ == '__main__':
    sample_string = "Qwen"
    try:
        first_letter = get_first_letter(sample_string)
        print(first_letter)
    except ValueError as e:
        print(e)