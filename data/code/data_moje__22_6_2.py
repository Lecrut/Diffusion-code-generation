import re
import string

def is_valid_password(password: str) -> bool:
    if not password or len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return False

    if len(password) > 0 and password[0] in string.punctuation:
        return False

    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count > 3:
                return False
        else:
            count = 1

    return True

if __name__ == '__main__':
    test_passwords = [
        "Str0ng!Pass",
        "weakpassword",
        "TooShort!1",
        "AAAAaa1!",
        "NoSpecial1aA",
        "NoLower!1a",
        "NoUpper!1a",
        "NoDigit!aa",
        "Valid!1aA",
        "TooLongRepeatingAAAAAAAAAaaa",
        "Perfect1!Pass"
    ]
    for p in test_passwords:
        result = is_valid_password(p)
        print(result)