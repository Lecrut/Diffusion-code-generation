def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

if __name__ == '__main__':
    test_scores = [95, 82, 76, 59, 45]
    for s in test_scores:
        print(get_grade(s))