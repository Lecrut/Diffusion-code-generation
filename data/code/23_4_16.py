class GradeCalculator:
    def __init__(self):
        self._grade_ranges = [
            (90, float('inf'), 'A'),
            (80, 89, 'B'),
            (70, 79, 'C'),
            (60, 69, 'D'),
            (0, 59, 'F')
        ]

    def get_letter_grade(self, score: float) -> str:
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        
        for min_score, max_score, grade in self._grade_ranges:
            if min_score <= score <= max_score:
                return grade
        raise ValueError("Invalid score range")

if __name__ == '__main__':
    calculator = GradeCalculator()
    test_scores = [95, 82, 76, 65, 59]
    for score in test_scores:
        print(calculator.get_letter_grade(score))