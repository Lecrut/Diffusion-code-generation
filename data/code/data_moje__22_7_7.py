def check_password_strength(password):
    if not isinstance(password, str) or len(password) == 0:
        return 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    strength = 0
    if has_upper:
        strength |= 0b1
    if has_lower:
        strength |= 0b10
    if has_digit:
        strength |= 0b100
    if has_special:
        strength |= 0b1000

    return strength

if __name__ == '__main__':
    sample_passwords = [
        "Hello",
        "hello123",
        "Hello123",
        "Hello123!",
        "",
        "12345",
        "ABCDEF",
        "!@#$%",
        "StrongP@ssw0rd!"
    ]

    for pwd in sample_passwords:
        result = check_password_strength(pwd)
        print(result)