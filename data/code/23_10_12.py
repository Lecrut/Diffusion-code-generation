def get_grade(score):
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
    scores = [95, 82, 71, 59, 100]
    for s in scores:
        print(f"Score {s} is grade {get_grade(s)}")