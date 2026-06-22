def get_grade(score):
    thresholds = [90, 80, 70, 60]
    grades = ['A', 'B', 'C', 'D', 'F']
    grade_index = 5
    for i, threshold in enumerate(thresholds):
        if score >= threshold:
            grade_index = i
            break
    return grades[grade_index]

if __name__ == '__main__':
    result = get_grade(72)
    print(result)