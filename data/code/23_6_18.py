def get_grade(score: float) -> str:
    if score >= 90.0:
        return "A"
    if score >= 80.0:
        return "B"
    if score >= 70.0:
        return "C"
    if score >= 60.0:
        return "D"
    return "F"

if __name__ == '__main__':
    print(get_grade(95.5))
    print(get_grade(82.3))
    print(get_grade(71.9))
    print(get_grade(59.99))
    print(get_grade(60.0))
    print(get_grade(100.0))
    print(get_grade(0.0))
    print(get_grade(-5.0))