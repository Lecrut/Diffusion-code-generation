def get_letter_grade(score):
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
    scores = [95, 82, 70, 65, 59]
    for score in scores:
        print(get_letter_grade(score))