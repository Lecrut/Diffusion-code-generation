import operator

def scores_to_grades(scores):
    def single_score_to_grade(score):
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

    return list(map(single_score_to_grade, scores))

if __name__ == '__main__':
    sample_scores = [92, 85, 73, 65, 58, 100, 0, 79, 89, 60]
    grades = scores_to_grades(sample_scores)
    print(grades)