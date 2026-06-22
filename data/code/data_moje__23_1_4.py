def convert_scores_to_grades(raw_scores):
    grade_boundaries = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }
    
    def get_letter_grade(score):
        for grade, (min_score, max_score) in grade_boundaries.items():
            if min_score <= score <= max_score:
                return grade
        return 'F'

    return [get_letter_grade(score) for score in raw_scores]

if __name__ == '__main__':
    raw_scores = [95, 88, 76, 65, 54, 100]
    letter_grades = convert_scores_to_grades(raw_scores)
    print(letter_grades)