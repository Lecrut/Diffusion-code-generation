WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "letmein",
    "football", "shadow", "123123", "654321", "superman", "qazwsx", "michael",
    "login", "princess", "starwars", "solo", "hello", "charlie", "donald",
    "password1", "qwerty123", "admin", "root", "pass", "test", "guest"
}

def has_sequential_characters(password, length=3):
    if len(password) < length:
        return False
    for i in range(len(password) - length + 1):
        segment = password[i:i + length].lower()
        is_sequential = True
        for j in range(1, len(segment)):
            if ord(segment[j]) != ord(segment[j - 1]) + 1:
                is_sequential = False
                break
        if is_sequential:
            return True
    return False

def validate_password_strength(password):
    if not password:
        return False

    if password.lower() in WEAK_PASSWORDS:
        return False

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    char_types_present = sum([has_upper, has_lower, has_digit, has_special])
    if char_types_present < 3:
        return False

    if has_sequential_characters(password):
        return False

    return True

if __name__ == '__main__':
    test_passwords = [
        "password",
        "12345678",
        "Str0ngP@ss!",
        "Abcdefgh",
        "Short1!",
        "Hello123",
        "MyS3cur3P@ssw0rd!",
        "qwertyuiop",
        "Aa1!",
        "Valid1Pass#9"
    ]

    results = {pwd: validate_password_strength(pwd) for pwd in test_passwords}
    for pwd, is_strong in results.items():
        print(f"{pwd}: {is_strong}")