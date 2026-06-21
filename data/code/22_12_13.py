import string

def check_password_strength(password):
    length = len(password)
    if length < 12:
        return False, 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    upper_mask = 0
    lower_mask = 0
    digit_mask = 0
    special_mask = 0

    upper_chars = set(string.ascii_uppercase)
    lower_chars = set(string.ascii_lowercase)
    digit_chars = set(string.digits)
    special_chars = set(string.punctuation)

    for char in password:
        if char in upper_chars:
            has_upper = True
            upper_mask |= 1 << (ord(char) - ord('A'))
        if char in lower_chars:
            has_lower = True
            lower_mask |= 1 << (ord(char) - ord('a'))
        if char in digit_chars:
            has_digit = True
            digit_mask |= 1 << (ord(char) - ord('0'))
        if char in special_chars:
            has_special = True
            special_mask |= 1 << (ord(char) % 32)

    criteria_met = has_upper & has_lower & has_digit & has_special

    diversity_score = (
        bin(upper_mask).count('1') +
        bin(lower_mask).count('1') +
        bin(digit_mask).count('1') +
        bin(special_mask).count('1')
    )

    return criteria_met, diversity_score

if __name__ == '__main__':
    test_password = "Str0ng!Pass#2024"
    is_strong, score = check_password_strength(test_password)
    print(is_strong)
    print(score)