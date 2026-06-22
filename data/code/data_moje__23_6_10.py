def get_grade(score: float) -> str:
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

if __name__ == "__main__":
    print(get_grade(95.5))
    print(get_grade(82.0))
    print(get_grade(69.99))
    print(get_grade(59.5))
    print(get_grade(100.0))
    print(get_grade(0.0))