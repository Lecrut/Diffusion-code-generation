def validate_password(password, username, email):
    if not password or len(password) < 8:
        return False
    username_lower = username.lower()
    if username_lower and username_lower in password.lower():
        return False
    email_domain = ""
    if email and "@" in email:
        email_domain = email.split("@")[1].lower()
    if email_domain and email_domain in password.lower():
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")
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
    return True

if __name__ == '__main__':
    sample_password = "Str0ng!P@ss"
    sample_username = "johndoe"
    sample_email = "johndoe@example.com"
    result = validate_password(sample_password, sample_username, sample_email)
    print(result)
    
    weak_password = "john123"
    result2 = validate_password(weak_password, sample_username, sample_email)
    print(result2)
    
    bad_password = "Example1!"
    result3 = validate_password(bad_password, sample_username, sample_email)
    print(result3)