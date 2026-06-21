def score_password(password: str) -> int:
    if not password:
        return 0
    length_score = min(len(password) * 1, 5)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    diversity_count = sum([has_lower, has_upper, has_digit, has_symbol])
    diversity_score = min(diversity_count * 1.5, 5)
    total_score = length_score + diversity_score
    return int(min(total_score, 10))

if __name__ == '__main__':
    sample_password = "MyStr0ng!Pass"
    result = score_password(sample_password)
    print(result)