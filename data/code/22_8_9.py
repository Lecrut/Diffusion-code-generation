def validate_password_strength(password, common_words=None):
    if common_words is None:
        common_words = [
            "password", "123456", "12345678", "qwerty", "abc123",
            "monkey", "1234567", "letmein", "trustno1", "dragon",
            "baseball", "iloveyou", "master", "sunshine", "ashley",
            "bailey", "shadow", "123123", "654321", "superman",
            "qazwsx", "michael", "football", "password1", "password123",
            "welcome", "jesus", "ninja", "mustang", "password2"
        ]
    
    if len(password) < 8:
        return False
    
    password_lower = password.lower()
    for word in common_words:
        if word in password_lower:
            return False
    
    return True

if __name__ == '__main__':
    sample_passwords = [
        "short",
        "password123",
        "MyS3cur3P@ss!",
        "qwertyuiop",
        "longbutweakpassword",
        "Str0ng!P@ssw0rd",
        "12345678",
        "abc123xyz"
    ]
    
    for pwd in sample_passwords:
        result = validate_password_strength(pwd)
        print(result)