import re

def validate_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]", password):
        return False
    return True

if __name__ == '__main__':
    result1 = validate_password_strength("ValidP@ss1")
    print(result1)
    result2 = validate_password_strength("weak")
    print(result2)
    result3 = validate_password_strength("NoSpecial1aA")
    print(result3)
    result4 = validate_password_strength("12345678")
    print(result4)
    result5 = validate_password_strength("UPPER1a!")
    print(result5)