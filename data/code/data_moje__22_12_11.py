import string

def check_password_strength(password):
    if not password:
        return False
    has_lower = 0
    has_upper = 0
    has_digit = 0
    has_special = 0
    lower_set = set(string.ascii_lowercase)
    upper_set = set(string.ascii_uppercase)
    digit_set = set(string.digits)
    special_set = set(string.punctuation)
    for char in password:
        if char in lower_set:
            has_lower = 1
        elif char in upper_set:
            has_upper = 1
        elif char in digit_set:
            has_digit = 1
        elif char in special_set:
            has_special = 1
    mask = 0
    if has_lower:
        mask |= 1
    if has_upper:
        mask |= 2
    if has_digit:
        mask |= 4
    if has_special:
        mask |= 8
    if len(password) < 12:
        return False
    if mask != 15:
        return False
    consecutive_count = 0
    for i in range(len(password) - 1):
        if ord(password[i]) + 1 == ord(password[i + 1]):
            consecutive_count += 1
        else:
            consecutive_count = 0
        if consecutive_count >= 3:
            return False
    return True

if __name__ == '__main__':
    test_string = "SecureP@ssw0rd12!"
    result = check_password_strength(test_string)
    print(result)