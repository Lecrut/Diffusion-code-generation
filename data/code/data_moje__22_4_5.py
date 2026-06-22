def score_password_strength(password):
    if not password:
        return 0
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    diversity = sum([has_lower, has_upper, has_digit, has_special])
    length_score = min(length * 10 // 20, 4)
    diversity_score = min(diversity * 1.5, 3)
    bonus = 3 if length >= 12 and diversity >= 4 else 0
    total = length_score + diversity_score + bonus
    return min(int(total), 10)

if __name__ == '__main__':
    print(score_password_strength("MyP@ssw0rd123"))
    print(score_password_strength("weak"))
    print(score_password_strength("Str0ng!Pass!2024#"))