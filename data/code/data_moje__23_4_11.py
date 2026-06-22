class GradePolicy:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def get_grade(self, score):
        for grade, threshold in self.thresholds:
            if score >= threshold:
                return grade
        return 'F'

class GradeCalculator:
    def __init__(self, policy):
        self.policy = policy

    def calculate(self, score):
        return self.policy.get_grade(score)

if __name__ == '__main__':
    thresholds = [('A', 90), ('B', 80), ('C', 70), ('D', 60), ('F', 0)]
    policy = GradePolicy(thresholds)
    calculator = GradeCalculator(policy)
    scores = [95, 85, 75, 65, 55]
    for score in scores:
        print(calculator.calculate(score))