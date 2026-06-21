def validate_password(password, username, email):
    if len(password) < 8:
        return False

    if username:
        if username.lower() in password.lower():
            return False

    if email:
        if "@" in email:
            domain = email.split("@")[-1].lower()
        else:
            domain = email.lower()
        if domain in password.lower():
            return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()-_=+[]{}|;:,.<>?/~`")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    required = sum([has_upper, has_lower, has_digit, has_special])
    if required < 3:
        return False

    return True

if __name__ == '__main__':
    result = validate_password("MyStr0ng!Pass", "john", "john@example.com")
    print(result)

    result2 = validate_password("john123456", "john", "john@example.com")
    print(result2)

    result3 = validate_password("Complex#Pass99", "jane", "jane@test.org")
    print(result3)