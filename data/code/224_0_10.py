class ScoreCalculator:
    def __init__(self, scores):
        self.scores = scores

    def calculate_mean(self):
        if not self.scores:
            return None
        total_score = sum(self.scores)
        count = len(self.scores)
        mean_score = total_score / count
        return mean_score

if __name__ == '__main__':
    calculator = ScoreCalculator([10, 20, 30, 40, 50])
    print(calculator.calculate_mean())