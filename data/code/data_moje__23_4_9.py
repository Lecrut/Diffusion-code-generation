class GradeThresholds:
    def __init__(self):
        self.thresholds = [
            (90, "A"),
            (80, "B"),
            (70, "C"),
            (60, "D"),
            (0, "F"),
        ]

    def get_grade(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for threshold, grade in self.thresholds:
            if score >= threshold:
                return grade
        return "F"

class Grader:
    def __init__(self, thresholds=None):
        if thresholds is None:
            self.thresholds = GradeThresholds()
        else:
            self.thresholds = thresholds

    def determine_grade(self, score):
        return self.thresholds.get_grade(score)

if __name__ == '__main__':
    grader = Grader()
    scores = [95, 85, 75, 65, 55, 100, 0]
    for score in scores:
        print(f"Score {score}: {grader.determine_grade(score)}")