def get_grade(score: float) -> str:
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
    print(get_grade(95.0))
    print(get_grade(85.5))
    print(get_grade(70.0))
    print(get_grade(60.0))
    print(get_grade(50.0))
    print(get_grade(0.0))
    print(get_grade(100.0))
    print(get_grade(89.9))
    print(get_grade(59.9))