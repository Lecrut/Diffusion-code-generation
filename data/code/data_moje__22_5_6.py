def validate_password(username, email, password):
    username_lower = username.lower()
    domain_lower = email.split('@')[-1].lower()
    password_lower = password.lower()
    
    if len(password) < 8:
        return False
    
    if username_lower in password_lower:
        return False
    
    if domain_lower in password_lower:
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
            
        if has_upper and has_lower and has_digit and has_special:
            return True
            
    return False

if __name__ == '__main__':
    username = 'john_doe'
    email = 'john@example.com'
    password1 = 'WeakPass1!'
    password2 = 'johnDoe1234!Safe'
    password3 = 'Str0ng#Pass!'
    
    result1 = validate_password(username, email, password1)
    result2 = validate_password(username, email, password2)
    result3 = validate_password(username, email, password3)
    
    print(f"{result1}, {result2}, {result3}")