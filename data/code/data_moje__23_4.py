class GradeCalculator:
    def __init__(self, grading_scale):
        self.grading_scale = grading_scale

    def determine_grade(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for min_score, grade in sorted(self.grading_scale.items(), reverse=True):
            if score >= min_score:
                return grade
        return "F"

if __name__ == "__main__":
    scale = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        0: "F"
    }
    calculator = GradeCalculator(scale)
    test_scores = [95, 82, 76, 59, 60]
    for s in test_scores:
        print(calculator.determine_grade(s))