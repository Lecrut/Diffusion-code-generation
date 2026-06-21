def _check_chars(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    return has_lower, has_upper, has_digit, has_special

def calculate_length_score(length):
    if length == 0:
        return 0
    base = min(length, 20)
    if base < 4:
        return 1
    elif base < 8:
        return 2
    elif base < 12:
        return 3
    elif base < 16:
        return 4
    else:
        return 5

def score_password_strength(password):
    if not password:
        return 0
    has_lower, has_upper, has_digit, has_special = _check_chars(password)
    diversity = int(has_lower) + int(has_upper) + int(has_digit) + int(has_special)
    diversity_component = min(diversity * 2, 8)
    length_component = calculate_length_score(len(password))
    total = diversity_component + length_component
    return min(max(total, 0), 10)

if __name__ == '__main__':
    print(score_password_strength('short'))
    print(score_password_strength('LongerPass123!'))
    print(score_password_strength('1234567890'))
    print(score_password_strength('ALLCAPS123'))
    print(score_password_strength(''))