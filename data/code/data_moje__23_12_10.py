def assign_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    scores = [100, 95, 85, 75, 65, 55, 0, 60, 70, 80, 90]
    grades = [assign_grade(s) for s in scores]
    for s, g in zip(scores, grades):
        print(f"{s}: {g}")