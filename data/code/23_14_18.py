def calculate_grade(score: float, thresholds: tuple = None) -> str:
    if thresholds is None:
        thresholds = (90, 80, 70, 60)
    if score >= thresholds[0]:
        return 'A'
    elif score >= thresholds[1]:
        return 'B'
    elif score >= thresholds[2]:
        return 'C'
    elif score >= thresholds[3]:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    print(calculate_grade(92))