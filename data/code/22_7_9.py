def check_password_strength(password):
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0

    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_upper = 1
        if 97 <= code <= 122:
            has_lower = 1
        if 48 <= code <= 57:
            has_digit = 1
        if not (48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122):
            has_special = 1

    strength = (has_upper << 3) | (has_lower << 2) | (has_digit << 1) | has_special
    return strength

if __name__ == '__main__':
    sample_passwords = ["abc", "ABC", "123", "!@#", "Abc123!@#", "Hello"]
    for pwd in sample_passwords:
        result = check_password_strength(pwd)
        print(result)