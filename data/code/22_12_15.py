import string

def check_password_strength(password):
    if not password:
        return (False, 0, {'length': 0, 'has_upper': False, 'has_lower': False, 'has_digit': False, 'has_special': False, 'charset_bits': 0, 'meets_length': False, 'meets_complexity': False})
    length = len(password)
    upper_set = set(string.ascii_uppercase)
    lower_set = set(string.ascii_lowercase)
    digit_set = set(string.digits)
    special_set = set(string.punctuation)
    has_upper = any((c in upper_set for c in password))
    has_lower = any((c in lower_set for c in password))
    has_digit = any((c in digit_set for c in password))
    has_special = any((c in special_set for c in password))
    charset_bits = 0
    charset_bits |= 1 if has_upper else 0
    charset_bits |= 2 if has_lower else 0
    charset_bits |= 4 if has_digit else 0
    charset_bits |= 8 if has_special else 0
    meets_length = length >= 12
    meets_complexity = charset_bits & 1 and charset_bits & 2 and charset_bits & 4 and charset_bits & 8
    is_strong = meets_length and meets_complexity
    strength_score = 0
    if meets_length:
        strength_score += 40
    if meets_complexity:
        strength_score += 40
    if length >= 16:
        strength_score += 10
    if length >= 20:
        strength_score += 10
    return (is_strong, strength_score, {'length': length, 'has_upper': has_upper, 'has_lower': has_lower, 'has_digit': has_digit, 'has_special': has_special, 'charset_bits': charset_bits, 'meets_length': meets_length, 'meets_complexity': meets_complexity})
if __name__ == '__main__':
    test_password = 'Tr0ub4dor&3'
    is_strong, score, details = check_password_strength(test_password)
    print((is_strong, score, details))