import sys

def check_password_types(password):
    if not isinstance(password, str):
        return False
    if len(password) == 0:
        return False
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    lower_mask = 0b11111111111111111111111111111110
    upper_mask = 0b10111111111111111111111111111111
    digit_mask = 0b10111111111111111111111111111111
    special_chars = set("!@#$%^&*()-_=+[]{}|;:,.<>?")
    for char in password:
        code = ord(char)
        if 97 <= code <= 122:
            has_lower = 1
        elif 65 <= code <= 90:
            has_upper = 1
        elif 48 <= code <= 57:
            has_digit = 1
        elif char in special_chars:
            has_special = 1
    return (has_lower & has_upper & has_digit & has_special) == 1

if __name__ == '__main__':
    sample_passwords = [
        "Password1!",
        "weak",
        "NoSpecial1",
        "ALLUPPER1!",
        "lowercase1!",
        "12345!@#$",
        "Str0ngP@ss"
    ]
    for pwd in sample_passwords:
        result = check_password_types(pwd)
        print(f"{pwd}: {result}")