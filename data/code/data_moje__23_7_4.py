def get_grade(score, grade_boundaries):
    sorted_scores = sorted(grade_boundaries.items(), key=lambda item: item[0], reverse=True)
    for boundary, grade in sorted_scores:
        if score >= boundary:
            return grade
    return "F"

if __name__ == '__main__':
    grade_boundaries = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
    score = 85
    result = get_grade(score, grade_boundaries)
    print(result)