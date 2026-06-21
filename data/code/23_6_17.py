def score_to_grade(score: float) -> str:
    if score < 0.0 or score > 100.0:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    print(score_to_grade(95.5))
    print(score_to_grade(87.3))
    print(score_to_grade(72.1))
    print(score_to_grade(65.0))
    print(score_to_grade(59.9))
    print(score_to_grade(100.0))
    print(score_to_grade(0.0))
    print(score_to_grade(89.99999999999999))
    print(score_to_grade(90.00000000000001))