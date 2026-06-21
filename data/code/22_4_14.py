def score_password(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    length_score = min(10 * (length / 20), 6) if length > 0 else 0
    diversity_score = 4 * (diversity_count / 4)
    final_score = length_score + diversity_score
    return min(10, max(0, int(final_score)))

if __name__ == '__main__':
    test_password = "MySecureP@ss123"
    result = score_password(test_password)
    print(result)