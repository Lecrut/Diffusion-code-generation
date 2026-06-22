import re
SPECIAL_CHARS = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
UPPER_PATTERN = re.compile(r'[A-Z]')
LOWER_PATTERN = re.compile(r'[a-z]')
DIGIT_PATTERN = re.compile(r'[0-9]')

def validate_password_strength(password):
    if len(password) < 8:
        return False
    if not UPPER_PATTERN.search(password):
        return False
    if not LOWER_PATTERN.search(password):
        return False
    if not DIGIT_PATTERN.search(password):
        return False
    if not SPECIAL_CHARS.search(password):
        return False
    return True

if __name__ == '__main__':
    print(validate_password_strength('Weak1!'))
    print(validate_password_strength('ValidPass1!'))
    print(validate_password_strength('AllLower1!'))
    print(validate_password_strength('AllUpper1!'))
    print(validate_password_strength('NoDigit!Aa'))
    print(validate_password_strength('ComplexP@ss99'))