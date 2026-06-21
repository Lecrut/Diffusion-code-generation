class GradeBoundary:
    def __init__(self, minimum, maximum, grade):
        self.minimum = minimum
        self.maximum = maximum
        self.grade = grade

class GradingScheme:
    def __init__(self):
        self.boundaries = [
            GradeBoundary(90, 100, "A"),
            GradeBoundary(80, 89, "B"),
            GradeBoundary(70, 79, "C"),
            GradeBoundary(60, 69, "D"),
            GradeBoundary(0, 59, "F")
        ]
    def get_grade_for(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for boundary in self.boundaries:
            if boundary.minimum <= score <= boundary.maximum:
                return boundary.grade
        raise ValueError("No grade found for score")

if __name__ == "__main__":
    scheme = GradingScheme()
    score = 85
    grade = scheme.get_grade_for(score)
    print(grade)