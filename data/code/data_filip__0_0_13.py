def extract_digits_to_int(mixed_string):
    digits = [char for char in mixed_string if char.isdigit()]
    if not digits:
        return 0
    return int(''.join(digits))

if __name__ == '__main__':
    result = extract_digits_to_int("abc123def456")
    print(result)
    result2 = extract_digits_to_int("no digits here!")
    print(result2)