class GradeThresholds:
    def __init__(self):
        self.thresholds = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
        ]

    def get_grade(self, score):
        for threshold, grade in self.thresholds:
            if score >= threshold:
                return grade
        return 'F'

class GradeCalculator:
    def __init__(self, thresholds=None):
        if thresholds is None:
            self.thresholds = GradeThresholds()
        else:
            self.thresholds = thresholds

    def get_letter_grade(self, score):
        return self.thresholds.get_grade(score)

if __name__ == '__main__':
    calculator = GradeCalculator()
    print(calculator.get_letter_grade(95))
    print(calculator.get_letter_grade(85))
    print(calculator.get_letter_grade(75))
    print(calculator.get_letter_grade(65))
    print(calculator.get_letter_grade(55))