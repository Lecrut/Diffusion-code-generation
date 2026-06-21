def score_password_strength(password):
    length = len(password)
    if length == 0:
        return 0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    diversity_score = sum([has_lower, has_upper, has_digit, has_special])
    length_factor = min(length / 12.0, 1.0)
    score = (length_factor * 5) + (diversity_score * 1.25)
    return min(round(score), 10)

if __name__ == '__main__':
    print(score_password_strength("Password123!"))
    print(score_password_strength("weak"))
    print(score_password_strength("STRONGpass99!@#"))