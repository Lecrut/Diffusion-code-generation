def score_password_strength(password):
    if not password:
        return 0
    score = 0
    length = len(password)
    if length >= 8:
        score += 2
    if length >= 12:
        score += 2
    if length >= 16:
        score += 1
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
    diversity = sum([has_lower, has_upper, has_digit, has_special])
    if diversity == 4:
        score += 4
    elif diversity == 3:
        score += 3
    elif diversity == 2:
        score += 1
    if score > 10:
        return 10
    return score

if __name__ == '__main__':
    print(score_password_strength("password123"))
    print(score_password_strength("Str0ng!Pass"))
    print(score_password_strength("short"))
    print(score_password_strength("VeryLongAndSecurePassword123!"))