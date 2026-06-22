def get_grade(score: float) -> str:
    epsilon = 1e-9
    if score + epsilon < 0.0:
        return "Invalid"
    elif score - epsilon < 60.0:
        return "F"
    elif score - epsilon < 70.0:
        return "D"
    elif score - epsilon < 80.0:
        return "C"
    elif score - epsilon < 90.0:
        return "B"
    elif score - epsilon <= 100.0:
        return "A"
    else:
        return "Invalid"

if __name__ == '__main__':
    sample_scores = [95.5, 88.0, 74.3, 61.0, 59.9, 0.0, 100.0, -5.0, 101.0]
    for s in sample_scores:
        print(get_grade(s))