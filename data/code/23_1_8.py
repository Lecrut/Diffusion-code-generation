score_to_grade_map = {
    (90, 101): 'A',
    (80, 90): 'B',
    (70, 80): 'C',
    (60, 70): 'D',
    (0, 60): 'F'
}

def convert_scores_to_grades(raw_scores):
    grades = []
    for score in raw_scores:
        for (low, high), grade in score_to_grade_map.items():
            if low <= score < high:
                grades.append(grade)
                break
        else:
            grades.append('F')
    return grades

if __name__ == '__main__':
    sample_scores = [95, 82, 76, 61, 59, 45, 100, 30]
    results = convert_scores_to_grades(sample_scores)
    print(results)