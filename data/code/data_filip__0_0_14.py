def extract_digits_to_int(s):
    digits = [char for char in s if char.isdigit()]
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == '__main__':
    sample1 = "abc123def456"
    sample2 = "no_digits_here"
    sample3 = "7x8y9z"
    sample4 = ""
    print(extract_digits_to_int(sample1))
    print(extract_digits_to_int(sample2))
    print(extract_digits_to_int(sample3))
    print(extract_digits_to_int(sample4))