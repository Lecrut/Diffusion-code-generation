def extract_digits_to_integer(s: str) -> int:
    digits = [char for char in s if char.isdigit()]
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == '__main__':
    sample_input_1 = "abc123xyz"
    sample_input_2 = "no digits here"
    sample_input_3 = "9876543210"
    sample_input_4 = "1a2b3c4d5e"
    
    print(extract_digits_to_integer(sample_input_1))
    print(extract_digits_to_integer(sample_input_2))
    print(extract_digits_to_integer(sample_input_3))
    print(extract_digits_to_integer(sample_input_4))