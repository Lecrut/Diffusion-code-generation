def validate_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(not c.isalnum() for c in password):
        return False
    consecutive_count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            consecutive_count += 1
            if consecutive_count > 3:
                return False
        else:
            consecutive_count = 1
    return True

if __name__ == '__main__':
    test_cases = [
        "Pass1234!",
        "AAAA1234!",
        "StrongP@ss",
        "weak",
        "Aa1!Aa1!Aa1",
        "ValidP@ss123",
        "Toolongpassword1!"
    ]
    for case in test_cases:
        print(f"{case}: {validate_password_strength(case)}")