def convert_scores_to_grades(scores):
    grade_map = {
        (90, 100): 'A',
        (80, 89): 'B',
        (70, 79): 'C',
        (60, 69): 'D',
        (0, 59): 'F'
    }
    def get_grade(score):
        for (low, high), grade in grade_map.items():
            if low <= score <= high:
                return grade
        return 'Invalid'
    return [get_grade(score) for score in scores]

if __name__ == '__main__':
    sample_scores = [95, 87, 72, 65, 48, 100, 80, 70, 60, 0]
    print(convert_scores_to_grades(sample_scores))