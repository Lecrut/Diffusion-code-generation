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

if __name__ == '__main__':
    sample_scores = [95.5, 82.0, 73.4, 59.9, 45.0]
    for s in sample_scores:
        print(get_grade(s))