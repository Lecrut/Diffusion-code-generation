def extract_digits(mixed_string):
    if not mixed_string:
        return 0
    digits = [char for char in mixed_string if char.isdigit()]
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == '__main__':
    print(extract_digits("abc123def456"))
    print(extract_digits("no_digits_here"))
    print(extract_digits(""))
    print(extract_digits("123"))