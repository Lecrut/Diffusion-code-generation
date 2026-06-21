from typing import List, Tuple, Optional

class GradeRange:
    def __init__(self, minimum: int, maximum: int, label: str):
        self.minimum = minimum
        self.maximum = maximum
        self.label = label

    def contains(self, score: float) -> bool:
        return self.minimum <= score <= self.maximum

class GradingPolicy:
    def __init__(self, ranges: List[GradeRange]):
        self.ranges = sorted(ranges, key=lambda r: r.minimum, reverse=True)

    def find_grade(self, score: float) -> str:
        for grade_range in self.ranges:
            if grade_range.contains(score):
                return grade_range.label
        raise ValueError(f"Score {score} is outside all defined grading ranges")

class ScoreValidator:
    @staticmethod
    def validate(score: float) -> None:
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numeric value")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100 inclusive")

class GradeEvaluator:
    def __init__(self, policy: GradingPolicy, validator: ScoreValidator):
        self.policy = policy
        self.validator = validator

    def determine_grade(self, score: float) -> str:
        self.validator.validate(score)
        return self.policy.find_grade(score)

def create_default_policy() -> GradingPolicy:
    ranges = [
        GradeRange(90, 100, "A"),
        GradeRange(80, 89, "B"),
        GradeRange(70, 79, "C"),
        GradeRange(60, 69, "D"),
        GradeRange(0, 59, "F")
    ]
    return GradingPolicy(ranges)

if __name__ == '__main__':
    default_policy = create_default_policy()
    evaluator = GradeEvaluator(default_policy, ScoreValidator)
    sample_scores = [95, 82, 76, 64, 45]
    results = []
    for score in sample_scores:
        grade = evaluator.determine_grade(score)
        results.append(f"Score: {score}, Grade: {grade}")
    for result in results:
        print(result)