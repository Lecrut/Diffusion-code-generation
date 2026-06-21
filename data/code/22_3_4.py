def check_password(password):
    common_passwords = {
        "password", "123456", "12345678", "123456789", "1234567890",
        "1234", "qwerty", "abc123", "monkey", "master", "dragon",
        "111111", "baseball", "iloveyou", "trustno1", "sunshine",
        "letmein", "princess", "welcome", "shadow", "ashley",
        "football", "jesus", "michael", "ninja", "mustang",
        "123123", "654321", "superman", "qazwsx", "batman",
        "admin", "login", "hello", "charlie", "donald"
    }
    if password.lower() in common_passwords:
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
    return True

if __name__ == '__main__':
    sample_passwords = [
        "password",
        "MyStr0ng!Pass",
        "12345678",
        "short",
        "noDigitsHere!!",
        "Complex99#$"
    ]
    results = []
    for pwd in sample_passwords:
        is_valid = check_password(pwd)
        results.append(is_valid)
    print(results)