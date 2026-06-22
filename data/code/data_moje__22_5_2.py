def validate_password(password, username=None, email=None):
    if not password or not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/")
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    if username:
        username_lower = username.lower()
        if username_lower in password.lower():
            return False
    if email:
        at_index = email.find("@")
        if at_index != -1:
            domain = email[at_index + 1:].lower()
            if domain in password.lower():
                return False
    return True

if __name__ == '__main__':
    sample_username = "johndoe"
    sample_email = "johndoe@example.com"
    test_cases = [
        ("Short1!", sample_username, sample_email),
        ("NoSpecial1a", sample_username, sample_email),
        ("ValidPass1!", sample_username, sample_email),
        ("john1234!", sample_username, sample_email),
        ("example.com1!", sample_username, sample_email),
        ("Strong1!Abc", sample_username, sample_email),
    ]
    for pwd, user, em in test_cases:
        result = validate_password(pwd, user, em)
        print(result)