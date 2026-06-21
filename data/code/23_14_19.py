def get_grade(score: float, thresholds: dict = None) -> str:
    if thresholds is None:
        thresholds = {
            'A': 90,
            'B': 80,
            'C': 70,
            'D': 60,
            'F': 0
        }
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    for grade, threshold in thresholds.items():
        if score >= threshold:
            return grade
    return 'F'

if __name__ == '__main__':
    print(get_grade(92))