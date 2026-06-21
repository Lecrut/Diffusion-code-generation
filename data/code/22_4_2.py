def score_password_strength(password):
    if not password:
        return 0
    score = 0
    length = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        else:
            has_special = True
    score += min(length, 10)
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    return min(score, 10)

if __name__ == '__main__':
    sample_password = "P@ssw0rd!"
    result = score_password_strength(sample_password)
    print(result)