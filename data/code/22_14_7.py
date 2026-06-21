WEAK_PASSWORDS = {"password", "123456", "12345678", "qwerty", "abc123", "monkey", "master", "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "princess", "football", "shadow", "superman", "michael", "password1", "letmein", "123123", "654321", "qazwsx", "login", "starwars", "solo", "hello", "charlie", "donald", "qwerty123", "admin", "root", "pass", "test", "guest"}

def check_sequentiality(text):
    if len(text) < 3:
        return False
    for i in range(len(text) - 2):
        c1, c2, c3 = text[i], text[i + 1], text[i + 2]
        if ord(c2) == ord(c1) + 1 and ord(c3) == ord(c2) + 1:
            return True
        if ord(c2) == ord(c1) - 1 and ord(c3) == ord(c2) - 1:
            return True
    return False

def validate_password_strength(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    if password.lower() in WEAK_PASSWORDS:
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
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    if check_sequentiality(password) or check_sequentiality(password.lower()):
        return False
    return True

if __name__ == '__main__':
    sample_password = "Str0ng!Pass"
    result = validate_password_strength(sample_password)
    print(result)
    
    sample_weak = "password123"
    result_weak = validate_password_strength(sample_weak)
    print(result_weak)
    
    sample_sequential = "Abc123!@#"
    result_seq = validate_password_strength(sample_sequential)
    print(result_seq)