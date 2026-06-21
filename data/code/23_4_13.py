GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]

class ScoreValidator:
    def validate(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

class GradeMapping:
    def __init__(self, thresholds=None):
        self.thresholds = thresholds if thresholds is not None else GRADE_THRESHOLDS

    def map(self, score):
        for minimum, grade in self.thresholds:
            if score >= minimum:
                return grade
        return "F"

class GradeCalculator:
    def __init__(self, validator=None, mapping=None):
        self.validator = validator if validator is not None else ScoreValidator()
        self.mapping = mapping if mapping is not None else GradeMapping()

    def calculate(self, score):
        self.validator.validate(score)
        return self.mapping.map(score)

if __name__ == "__main__":
    calculator = GradeCalculator()
    print(calculator.calculate(95))
    print(calculator.calculate(85))
    print(calculator.calculate(72))
    print(calculator.calculate(60))
    print(calculator.calculate(45))