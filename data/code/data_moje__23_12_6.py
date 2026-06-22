def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError('Score must be a number')
    if score < 0 or score > 100:
        raise ValueError('Score must be between 0 and 100')
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
    sample_scores = [95, 85, 75, 65, 55, 0, 100, 89.5, 60.1, 59.9]
    for score in sample_scores:
        try:
            grade = assign_grade(score)
            print(f'Score: {score}, Grade: {grade}')
        except (TypeError, ValueError) as e:
            print(f'Score: {score}, Error: {e}')