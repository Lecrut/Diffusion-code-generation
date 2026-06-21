class GradeCalculator:
    def __init__(self, grade_thresholds):
        self.thresholds = grade_thresholds

    def determine_grade(self, score):
        for grade, threshold in self.thresholds.items():
            if score >= threshold:
                return grade
        return 'F'

if __name__ == '__main__':
    threshold_map = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    calculator = GradeCalculator(threshold_map)
    sample_scores = [95, 85, 72, 65, 50, 100, 0]
    results = [calculator.determine_grade(score) for score in sample_scores]
    for score, grade in zip(sample_scores, results):
        print(f"Score: {score}, Grade: {grade}")