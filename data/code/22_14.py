COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine",
    "princess", "football", "shadow", "superman", "michael", "password1"
}

def validate_password_strength(password):
    if not isinstance(password, str) or len(password) < 8:
        return False

    lower_password = password.lower()
    if lower_password in COMMON_WEAK_PASSWORDS:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return False

    if has_sequential_characters(password):
        return False

    return True

def has_sequential_characters(password):
    if len(password) < 3:
        return False

    lower_pass = password.lower()

    for i in range(len(lower_pass) - 2):
        c1 = ord(lower_pass[i])
        c2 = ord(lower_pass[i + 1])
        c3 = ord(lower_pass[i + 2])

        if c2 == c1 + 1 and c3 == c2 + 1:
            return True

        if c2 == c1 - 1 and c3 == c2 - 1:
            return True

    return False

if __name__ == '__main__':
    test_cases = [
        "password",
        "StrongP@ss1",
        "abcdef123!",
        "Str0ngP@ss",
        "abc123",
        "MyS3cur3P@ss!"
    ]

    for test in test_cases:
        result = validate_password_strength(test)
        print(f"{test}: {result}")