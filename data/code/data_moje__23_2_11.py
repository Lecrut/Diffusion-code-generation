def get_letter_grade(score):
    if not isinstance(score, int) or not (0 <= score <= 100):
        raise ValueError("Score must be an integer between 0 and 100")
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
    sample_scores = [95, 82, 70, 65, 50, 0, 100, 89, 79, 60]
    for s in sample_scores:
        print(get_letter_grade(s))