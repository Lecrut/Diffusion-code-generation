def validate_password_strength(password: str) -> bool:
    common_weak_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123", 
        "monkey", "1234567", "letmein", "trustno1", "dragon",
        "baseball", "iloveyou", "master", "sunshine", "ashley",
        "bailey", "passw0rd", "shadow", "123123", "654321",
        "superman", "qazwsx", "michael", "football", "password1",
        "password123", "welcome", "hello", "charlie", "donald"
    ]
    
    if not password:
        return False
    
    if len(password) < 8:
        return False
    
    if password.lower() in common_weak_passwords:
        return False
    
    if len(set(password.lower())) < 4:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    char_set = set()
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
        char_set.add(char)
    
    if not (has_upper and has_lower and (has_digit or has_special)):
        return False
    
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
            return False
    
    for i in range(len(password) - 2):
        if ord(password[i]) - 1 == ord(password[i+1]) and ord(password[i+1]) - 1 == ord(password[i+2]):
            return False
    
    return True

if __name__ == '__main__':
    test_passwords = ["P@ssw0rd1", "password", "123456", "Str0ng!Pass", "abc", "aA1!"]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"{result} for {pwd}")