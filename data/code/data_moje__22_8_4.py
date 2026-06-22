import re
import sys

COMMON_WORDS = [
    "password", "password1", "password123", "letmein", "welcome", "admin",
    "login", "monkey", "dragon", "master", "qwerty", "abc123", "111111",
    "123456", "12345678", "sunshine", "princess", "football", "iloveyou",
    "trustno1", "superman", "batman", "hello", "charlie", "donald", "access"
]

def validate_password_strength(password):
    if not isinstance(password, str):
        return {"valid": False, "errors": ["Password must be a string"]}
    
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    
    if len(password) > 128:
        errors.append("Password must not exceed 128 characters")
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    complexity_count = sum([has_upper, has_lower, has_digit, has_special])
    if complexity_count < 3:
        errors.append("Password must contain at least 3 of the following: uppercase, lowercase, digit, special character")
    
    password_lower = password.lower()
    for word in COMMON_WORDS:
        if word in password_lower:
            errors.append(f"Password contains common word: {word}")
            break
    
    repeated_char_pattern = re.compile(r'(.)\1{2,}')
    if repeated_char_pattern.search(password):
        errors.append("Password contains 3 or more repeated characters in a row")
    
    sequence_pattern = re.compile(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)')
    if sequence_pattern.search(password_lower):
        errors.append("Password contains a common sequential pattern")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "length": len(password)
    }

if __name__ == '__main__':
    test_passwords = [
        "SecureP@ssw0rd123!",
        "password123",
        "abC1!",
        "MyStr0ng!Pass",
        "qwerty1234"
    ]
    
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"Password: {pwd}")
        print(f"Valid: {result['valid']}")
        print(f"Errors: {result['errors']}")
        print(f"Length: {result['length']}")
        print("---")