class GradeRange:
    def __init__(self, minimum_score, maximum_score, grade):
        self.minimum_score = minimum_score
        self.maximum_score = maximum_score
        self.grade = grade

    def covers(self, score):
        return self.minimum_score <= score <= self.maximum_score

class GradeEvaluator:
    def __init__(self, ranges):
        self.ranges = ranges

    def evaluate(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for grade_range in self.ranges:
            if grade_range.covers(score):
                return grade_range.grade
        return "F"

def create_default_ranges():
    return [
        GradeRange(90, 100, "A"),
        GradeRange(80, 89, "B"),
        GradeRange(70, 79, "C"),
        GradeRange(60, 69, "D"),
        GradeRange(0, 59, "F"),
    ]

if __name__ == "__main__":
    ranges = create_default_ranges()
    evaluator = GradeEvaluator(ranges)
    test_scores = [95, 82, 77, 65, 55, 0, 100, 89.5]
    for score in test_scores:
        result = evaluator.evaluate(score)
        print(f"Score: {score} -> Grade: {result}")