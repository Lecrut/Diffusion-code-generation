def score_password_strength(password):
    if not password:
        return 0

    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    diversity_score = 0
    diversity_score += has_lower
    diversity_score += has_upper
    diversity_score += has_digit
    diversity_score += has_special

    length_factor = min(length / 12, 1.0)

    raw_score = (diversity_score * 2.5) + (length_factor * 5)

    return min(max(int(raw_score), 0), 10)

if __name__ == '__main__':
    print(score_password_strength('a'))
    print(score_password_strength('Password1!'))
    print(score_password_strength('MyS3cureP@ssw0rd!'))
    print(score_password_strength('short'))
    print(score_password_strength('A1'))
    print(score_password_strength('aaaaaaaaaaaaa'))
    print(score_password_strength('A1b2C3d4E5f6!@#'))