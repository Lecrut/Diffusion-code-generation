def score_password_strength(password):
    if not password:
        return 0

    length_score = min(len(password) * 0.5, 4.0)

    has_lower = bool(any(c.islower() for c in password))
    has_upper = bool(any(c.isupper() for c in password))
    has_digit = bool(any(c.isdigit() for c in password))
    has_special = bool(any(not c.isalnum() for c in password))

    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
    diversity_score = diversity_count * 1.5

    score = length_score + diversity_score

    return min(round(score), 10)

if __name__ == '__main__':
    samples = [
        '',
        'abc',
        'Abc1',
        'Abc1!',
        'P@ssw0rd!123'
    ]
    for pwd in samples:
        print(score_password_strength(pwd))