def determine_grade(score):
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
    sample_scores = [95, 82, 77, 64, 55, 90, 45]
    for score in sample_scores:
        grade = determine_grade(score)
        print(f"Score: {score}, Grade: {grade}")