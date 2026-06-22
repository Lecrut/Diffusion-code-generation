def validate_password(username, email, password):
    if len(password) < 8:
        return False
    
    if username.lower() in password.lower():
        return False
    
    if '@' in email:
        domain = email.split('@')[1]
        if domain.lower() in password.lower():
            return False
    
    return True

if __name__ == '__main__':
    user_name = "johndoe"
    user_email = "johndoe@example.com"
    weak_password = "mypassword_johndoe"
    strong_password = "xK9$mP2!qR7"
    
    result1 = validate_password(user_name, user_email, weak_password)
    print(result1)
    
    result2 = validate_password(user_name, user_email, strong_password)
    print(result2)