COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "passw0rd", "shadow", "123123", "654321"
}

def validate_password_strength(password):
    if not password:
        return False
    
    lower_len = len(password)
    if lower_len < 8 or lower_len > 128:
        return False
    
    lower_password = password.lower()
    if lower_password in COMMON_WEAK_PASSWORDS:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    if char_types < 3:
        return False
    
    for i in range(len(password) - 3):
        substring = password[i:i+4]
        is_sequential = True
        for j in range(1, 4):
            if ord(substring[j]) != ord(substring[j-1]) + 1:
                is_sequential = False
                break
        if is_sequential:
            return False
    
    sorted_password = sorted(password)
    for i in range(len(sorted_password) - 3):
        if sorted_password[i] == sorted_password[i+1] == sorted_password[i+2] == sorted_password[i+3]:
            return False
    
    return True

if __name__ == '__main__':
    test_passwords = [
        "password123",
        "P@ssw0rd!23",
        "abcd1234",
        "MyStr0ng!Pass",
        "12345678",
        "aaaa1111!A"
    ]
    results = [validate_password_strength(pw) for pw in test_passwords]
    print(results)