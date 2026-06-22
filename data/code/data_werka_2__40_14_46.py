def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        raise ValueError("Input string cannot be empty")

def get_first_letter(s):
    validate_input(s)
    return s[0]

if __name__ == '__main__':
    sample_string = "Qwen AI"
    first_letter = get_first_letter(sample_string)
    print(first_letter)