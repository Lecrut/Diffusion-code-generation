COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "password1", "123123", "welcome", "shadow"
}

def is_sequential(s: str, length: int = 3) -> bool:
    if len(s) < length:
        return False
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if substring.islower() or substring.isupper() or substring.isdigit():
            if substring.lower() == "qwe" or substring.lower() == "asd" or substring.lower() == "zxc":
                return True
            chars = substring
            is_ascending = True
            is_descending = True
            for j in range(1, len(chars)):
                if ord(chars[j]) != ord(chars[j-1]) + 1:
                    is_ascending = False
                if ord(chars[j]) != ord(chars[j-1]) - 1:
                    is_descending = False
            if is_ascending or is_descending:
                return True
    return False

def validate_password_strength(password: str) -> dict:
    result = {
        "is_valid": True,
        "reasons": []
    }
    
    if password.lower() in COMMON_WEAK_PASSWORDS:
        result["is_valid"] = False
        result["reasons"].append("Password is a common weak password")
    
    if len(password) < 8:
        result["is_valid"] = False
        result["reasons"].append("Password must be at least 8 characters long")
    
    if not any(c.islower() for c in password):
        result["is_valid"] = False
        result["reasons"].append("Password must contain lowercase letters")
    
    if not any(c.isupper() for c in password):
        result["is_valid"] = False
        result["reasons"].append("Password must contain uppercase letters")
    
    if not any(c.isdigit() for c in password):
        result["is_valid"] = False
        result["reasons"].append("Password must contain digits")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        result["is_valid"] = False
        result["reasons"].append("Password must contain special characters")
    
    if is_sequential(password, 3):
        result["is_valid"] = False
        result["reasons"].append("Password contains sequential characters")
    
    if len(result["reasons"]) == 0:
        result["reasons"].append("Password meets all requirements")
    
    return result

if __name__ == '__main__':
    test_passwords = ["SecureP@ss1", "password", "12345678", "MyStr0ng!Pass", "qwerty123"]
    for pwd in test_passwords:
        print(f"Password: {pwd} -> {validate_password_strength(pwd)}")