class GradeResult:
    def __init__(self, score, grade):
        self.score = score
        self.grade = grade

class GradeCalculator:
    def __init__(self):
        self.thresholds = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
        ]
        self.default_grade = 'F'

    def calculate(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        
        for threshold, grade in self.thresholds:
            if score >= threshold:
                return GradeResult(score, grade)
        
        return GradeResult(score, self.default_grade)

if __name__ == '__main__':
    calculator = GradeCalculator()
    sample_scores = [95, 85, 75, 65, 55]
    for score in sample_scores:
        result = calculator.calculate(score)
        print(f"Score: {result.score}, Grade: {result.grade}")