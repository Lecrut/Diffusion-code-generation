COMMON_WEAK_PASSWORDS = {"123456", "password", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine", "ashley", "bailey", "passw0rd", "shadow", "123123", "654321"}

def has_sequential_chars(password, length=3):
    if len(password) < length:
        return False
    for i in range(len(password) - length + 1):
        segment = password[i : i + length]
        if len(set(segment)) != length:
            continue
        first = ord(segment[0])
        second = ord(segment[1])
        third = ord(segment[2])
        if second == first + 1 and third == second + 1:
            return True
        if second == first - 1 and third == second - 1:
            return True
    return False

def validate_password_strength(password):
    if password.lower() in COMMON_WEAK_PASSWORDS:
        return False
    if len(password) < 8:
        return False
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if not (has_lower and has_upper and has_digit):
        return False
    if has_sequential_chars(password):
        return False
    return True

if __name__ == "__main__":
    test_passwords = ["SecurePass1", "password", "qwerty123", "Str0ngP@ss", "Abcdefg1"]
    results = {pwd: validate_password_strength(pwd) for pwd in test_passwords}
    print(results)