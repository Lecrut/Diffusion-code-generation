def convert_scores_to_grades(raw_scores, grade_boundaries=None):
    if grade_boundaries is None:
        grade_boundaries = [90, 80, 70, 60]
    
    grade_map = {
        (0, 60): 'F',
        (60, 70): 'D',
        (70, 80): 'C',
        (80, 90): 'B',
        (90, 101): 'A'
    }
    
    result = []
    for score in raw_scores:
        if score >= 90:
            result.append('A')
        elif score >= 80:
            result.append('B')
        elif score >= 70:
            result.append('C')
        elif score >= 60:
            result.append('D')
        else:
            result.append('F')
    return result

if __name__ == '__main__':
    scores = [95, 82, 74, 58, 100, 69]
    grades = convert_scores_to_grades(scores)
    print(grades)