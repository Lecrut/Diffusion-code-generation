def score_password_strength(password):
    if not password:
        return 0
    length_score = min(len(password) / 20, 1.0) * 4
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    diversity_score = (diversity_count / 4) * 6
    return min(round(length_score + diversity_score), 10)

if __name__ == '__main__':
    print(score_password_strength("abc"))
    print(score_password_strength("Abc123!@#"))
    print(score_password_strength("Aa1!"))
    print(score_password_strength(""))
    print(score_password_strength("password123"))