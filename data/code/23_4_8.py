GRADING_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
]

class ScoreValidator:
    def __init__(self, min_value=0, max_value=100):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numeric type")
        if score < self.min_value or score > self.max_value:
            raise ValueError("Score out of range")

class GradeLookup:
    def __init__(self, thresholds):
        self.thresholds = sorted(thresholds, key=lambda x: x[0], reverse=True)
        self.fallback = "F"

    def find_grade(self, score):
        for threshold, grade in self.thresholds:
            if score >= threshold:
                return grade
        return self.fallback

class GradeService:
    def __init__(self, validator=None, lookup=None):
        self.validator = validator or ScoreValidator()
        self.lookup = lookup or GradeLookup(GRADING_THRESHOLDS)

    def determine_letter_grade(self, score):
        self.validator.validate(score)
        return self.lookup.find_grade(score)

if __name__ == '__main__':
    service = GradeService()
    test_scores = [95, 82, 75, 60, 45, 100, 0]
    for s in test_scores:
        grade = service.determine_letter_grade(s)
        print(f"Score: {s}, Grade: {grade}")