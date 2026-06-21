def validate_password(username, email, password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_characters = set("!@#$%^&*()-_=+[]{}|;:',.<>?/")
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    
    if username and username in password:
        return False
    
    if email:
        domain = email.split('@')[-1] if '@' in email else ''
        if domain and domain in password:
            return False
    
    return True

if __name__ == '__main__':
    username = "john_doe"
    email = "john@example.com"
    password_good = "Str0ng!Pass"
    password_bad_user = "Str0ng!John"
    password_bad_domain = "Str0ng!example"
    
    result_good = validate_password(username, email, password_good)
    result_bad_user = validate_password(username, email, password_bad_user)
    result_bad_domain = validate_password(username, email, password_bad_domain)
    
    print(f"Good password valid: {result_good}")
    print(f"Bad password (user) valid: {result_bad_user}")
    print(f"Bad password (domain) valid: {result_bad_domain}")