def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
if __name__ == '__main__':
    sample_scores = [95, 82, 71, 63, 55, 90, 89]
    for score in sample_scores:
        result = determine_grade(score)
        print(f"Score: {score}, Grade: {result}")