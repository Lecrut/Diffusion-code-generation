def score_password_strength(password):
    score = 0
    length = len(password)
    if length >= 8:
        score += 2
    if length >= 12:
        score += 2
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    diversity = sum([has_lower, has_upper, has_digit, has_symbol])
    if diversity == 1:
        score += 1
    if diversity == 2:
        score += 2
    if diversity == 3:
        score += 3
    if diversity == 4:
        score += 4
    return min(score, 10)

if __name__ == '__main__':
    print(score_password_strength("abc"))
    print(score_password_strength("Abc123"))
    print(score_password_strength("StrongP@ssw0rd"))
    print(score_password_strength("aB3#xY9$z"))
    print(score_password_strength("1234567890"))