class GradeCalculator:
    def __init__(self, grading_scheme=None):
        if grading_scheme is None:
            grading_scheme = [
                (90, 100, 'A'),
                (80, 89, 'B'),
                (70, 79, 'C'),
                (60, 69, 'D'),
                (0, 59, 'F')
            ]
        self.grading_scheme = grading_scheme

    def calculate_grade(self, score):
        for lower_bound, upper_bound, grade in self.grading_scheme:
            if lower_bound <= score <= upper_bound:
                return grade
        raise ValueError(f"Score {score} is outside all defined grade ranges")

if __name__ == '__main__':
    calculator = GradeCalculator()
    scores = [95, 87, 72, 65, 50, 100, 0]
    for score in scores:
        grade = calculator.calculate_grade(score)
        print(f"Score: {score}, Grade: {grade}")