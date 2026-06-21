class GradeCalculator:
    def __init__(self, grade_boundaries):
        self.grade_boundaries = grade_boundaries

    def calculate_grade(self, score):
        for grade, threshold in self.grade_boundaries:
            if score >= threshold:
                return grade
        return 'F'

if __name__ == '__main__':
    boundaries = [
        ('A', 90),
        ('B', 80),
        ('C', 70),
        ('D', 60)
    ]
    calculator = GradeCalculator(boundaries)
    test_score = 85
    result = calculator.calculate_grade(test_score)
    print(result)
    test_score_2 = 95
    result_2 = calculator.calculate_grade(test_score_2)
    print(result_2)
    test_score_3 = 55
    result_3 = calculator.calculate_grade(test_score_3)
    print(result_3)