class GradeCalculator:
    def __init__(self, grade_ranges=None):
        if grade_ranges is None:
            self.grade_ranges = [
                (90, 100, 'A'),
                (80, 89, 'B'),
                (70, 79, 'C'),
                (60, 69, 'D'),
                (0, 59, 'F')
            ]
        else:
            self.grade_ranges = grade_ranges

    def get_letter_grade(self, score):
        for lower, upper, grade in self.grade_ranges:
            if lower <= score <= upper:
                return grade
        raise ValueError("Score out of defined range")

if __name__ == '__main__':
    calculator = GradeCalculator()
    scores = [95, 85, 75, 65, 55, 100, 0]
    for score in scores:
        print(calculator.get_letter_grade(score))