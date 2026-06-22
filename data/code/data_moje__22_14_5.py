COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "master", "dragon", "111111", "baseball",
    "iloveyou", "trustno1", "sunshine", "princess", "football",
    "shadow", "superman", "michael", "letmein", "password1"
}

def _has_sequential_chars(password, length=3):
    for i in range(len(password) - length + 1):
        segment = password[i:i + length]
        if all(ord(segment[j]) == ord(segment[0]) + j for j in range(len(segment))):
            return True
        if all(ord(segment[j]) == ord(segment[0]) - j for j in range(len(segment))):
            return True
    return False

def validate_password_strength(password):
    if not password:
        return False

    if len(password) < 8:
        return False

    if password.lower() in COMMON_WEAK_PASSWORDS:
        return False

    if _has_sequential_chars(password):
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    character_types_present = sum([has_upper, has_lower, has_digit, has_special])
    if character_types_present < 3:
        return False

    return True

if __name__ == '__main__':
    test_passwords = [
        "password",
        "Short1!",
        "Str0ng!Pass",
        "abcdef123",
        "MyP@ssw0rd123",
        "12345678",
        "Aa1!bcdef",
        "Weakpass",
        "Strong@Pass1",
        "abcABC123!"
    ]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(result)