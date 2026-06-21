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
    print(score_to_grade(87.3))
    print(score_to_grade(72.1))
    print(score_to_grade(65.9))
    print(score_to_grade(45.0))
    print(score_to_grade(89.999999999))
    print(score_to_grade(90.000000001))