class GradeRange:
    def __init__(self, min_score, grade):
        self.min_score = min_score
        self.grade = grade

    def applies_to(self, score):
        return score >= self.min_score

class GradeService:
    def __init__(self, ranges):
        self.ranges = ranges

    def calculate_grade(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numeric value")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        
        for grade_range in self.ranges:
            if grade_range.applies_to(score):
                return grade_range.grade
        
        return "F"

DEFAULT_RANGES = [
    GradeRange(90, "A"),
    GradeRange(80, "B"),
    GradeRange(70, "C"),
    GradeRange(60, "D"),
    GradeRange(0, "F")
]

class GradeCalculator:
    def __init__(self, service):
        self.service = service

    def determine(self, score):
        return self.service.calculate_grade(score)

if __name__ == '__main__':
    service = GradeService(DEFAULT_RANGES)
    calculator = GradeCalculator(service)
    print(calculator.determine(95))
    print(calculator.determine(82))
    print(calculator.determine(75))
    print(calculator.determine(61))
    print(calculator.determine(45))