def score_password_strength(password):
    if not password:
        return 0
    length_score = min(len(password), 10)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    diversity_score = (diversity_count / 4) * 5
    total_score = length_score + diversity_score
    return min(max(0, total_score), 10)

if __name__ == '__main__':
    sample_password = "SecureP@ss123"
    print(score_password_strength(sample_password))