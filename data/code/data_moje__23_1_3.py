SCORE_TO_GRADE = {
    4.0: "A+",
    3.7: "A",
    3.3: "A-",
    3.0: "B+",
    2.7: "B",
    2.3: "B-",
    2.0: "C+",
    1.7: "C",
    1.3: "C-",
    1.0: "D+",
    0.7: "D",
    0.3: "D-",
    0.0: "F"
}

def convert_scores_to_grades(scores):
    grade_boundaries = sorted(SCORE_TO_GRADE.keys(), reverse=True)
    
    def get_grade(score):
        for boundary in grade_boundaries:
            if score >= boundary:
                return SCORE_TO_GRADE[boundary]
        return SCORE_TO_GRADE[0.0]
    
    return [get_grade(score) for score in scores]

if __name__ == '__main__':
    raw_scores = [4.0, 3.8, 3.35, 3.0, 2.8, 2.35, 2.0, 1.5, 1.0, 0.5, 0.0]
    grades = convert_scores_to_grades(raw_scores)
    print(grades)