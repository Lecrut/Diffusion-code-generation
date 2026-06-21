def score_to_grade(score: float) -> str:
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    print(score_to_grade(95.5))
    print(score_to_grade(88.0))
    print(score_to_grade(72.3))
    print(score_to_grade(65.1))
    print(score_to_grade(59.9))
    print(score_to_grade(100.0))
    print(score_to_grade(0.0))