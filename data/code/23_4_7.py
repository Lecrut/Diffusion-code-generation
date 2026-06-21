class GradeCalculator:
    def __init__(self, grading_scheme):
        self._scheme = grading_scheme

    def calculate_grade(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        
        for threshold, grade in reversed(self._scheme):
            if score >= threshold:
                return grade
        
        return "F"

class DefaultGradingScheme:
    def __init__(self):
        self._scheme = [
            (90, "A"),
            (80, "B"),
            (70, "C"),
            (60, "D"),
            (0, "F")
        ]

    def get_scheme(self):
        return self._scheme

if __name__ == '__main__':
    scheme_provider = DefaultGradingScheme()
    calculator = GradeCalculator(scheme_provider.get_scheme())
    
    scores = [95, 87, 72, 65, 58, 0, 100]
    for score in scores:
        grade = calculator.calculate_grade(score)
        print(f"Score: {score}, Grade: {grade}")