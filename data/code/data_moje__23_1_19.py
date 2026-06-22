SCORE_TO_GRADE = {
    (90, 101): 'A',
    (80, 90): 'B',
    (70, 80): 'C',
    (60, 70): 'D',
    (0, 60): 'F'
}

def grade_ranges_to_map():
    mapping = {}
    for min_score, max_score in SCORE_TO_GRADE:
        grade = SCORE_TO_GRADE[(min_score, max_score)]
        for score in range(min_score, max_score):
            mapping[score] = grade
    mapping[100] = 'A'
    return mapping

GRADE_MAP = grade_ranges_to_map()

def convert_scores_to_grades(scores):
    return [GRADE_MAP[score] for score in scores]

if __name__ == '__main__':
    raw_scores = [95, 82, 77, 61, 45, 100, 89, 70, 59]
    grades = convert_scores_to_grades(raw_scores)
    print(grades)