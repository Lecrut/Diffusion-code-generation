class GradeCalculator:
    def __init__(self, grade_thresholds):
        self.grade_thresholds = sorted(grade_thresholds, key=lambda x: x[0], reverse=True)

    def calculate_letter_grade(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for threshold, grade in self.grade_thresholds:
            if score >= threshold:
                return grade
        return self.grade_thresholds[-1][1]

if __name__ == '__main__':
    thresholds = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')]
    calculator = GradeCalculator(thresholds)
    print(calculator.calculate_letter_grade(95))
    print(calculator.calculate_letter_grade(82))
    print(calculator.calculate_letter_grade(75))
    print(calculator.calculate_letter_grade(65))
    print(calculator.calculate_letter_grade(55))