def assign_grade(score):
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
    sample_scores = [95, 87, 72, 64, 58, 100, 0, 60, 90, 89, 79, 70, 69]
    for score in sample_scores:
        print(assign_grade(score))