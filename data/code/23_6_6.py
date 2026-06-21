def calculate_grade(score: float) -> str:
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
    print(calculate_grade(95.5))
    print(calculate_grade(82.0))
    print(calculate_grade(70.0))
    print(calculate_grade(55.0))