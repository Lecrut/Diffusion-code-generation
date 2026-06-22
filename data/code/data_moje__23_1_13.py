def convert_scores_to_grades(scores):
    grade_boundaries = {
        90: 'A',
        80: 'B',
        70: 'C',
        60: 'D',
        0: 'F'
    }
    
    sorted_boundaries = sorted(grade_boundaries.items(), key=lambda x: x[0], reverse=True)
    
    def get_grade(score):
        for threshold, grade in sorted_boundaries:
            if score >= threshold:
                return grade
        return 'F'
    
    return [get_grade(score) for score in scores]

if __name__ == '__main__':
    raw_scores = [95, 82, 74, 65, 58, 40]
    letter_grades = convert_scores_to_grades(raw_scores)
    print(letter_grades)