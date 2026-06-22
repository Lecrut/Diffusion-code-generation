def get_grade(score: float, thresholds: dict = None) -> str:
    if thresholds is None:
        thresholds = {
            'A': 90,
            'B': 80,
            'C': 70,
            'D': 60
        }

    if score >= thresholds.get('A', 90):
        return 'A'
    elif score >= thresholds.get('B', 80):
        return 'B'
    elif score >= thresholds.get('C', 70):
        return 'C'
    elif score >= thresholds.get('D', 60):
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    print(get_grade(92))