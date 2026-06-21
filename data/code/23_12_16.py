def assign_letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
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
    sample_scores = [0, 59, 60, 69, 70, 79, 80, 89, 90, 100]
    grades = [assign_letter_grade(s) for s in sample_scores]
    print(grades)