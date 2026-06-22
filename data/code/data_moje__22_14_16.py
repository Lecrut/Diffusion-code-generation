def validate_password_strength(password: str) -> bool:
    common_weak_passwords = ["password", "123456", "12345678", "qwerty", "abc123", "monkey", "master", "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "princess", "football"]
    lower_common = [p.lower() for p in common_weak_passwords]
    if password.lower() in lower_common:
        return False
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    if not (has_upper and has_lower and has_digit):
        return False
    for i in range(len(password) - 2):
        c1 = ord(password[i])
        c2 = ord(password[i+1])
        c3 = ord(password[i+2])
        if (c2 == c1 + 1 and c3 == c2 + 1) or (c2 == c1 - 1 and c3 == c2 - 1):
            return False
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            count = 2
            j = i + 2
            while j < len(password) and password[j] == password[i]:
                count += 1
                j += 1
            if count >= 3:
                return False
    return True

if __name__ == '__main__':
    test_passwords = ["Str0ng!Pass", "password123", "12345678", "Str0ng!PassSSS", "Abc123"]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(result)