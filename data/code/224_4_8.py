class ScoreCalculator:
    def __init__(self, scores):
        if not scores:
            raise ValueError("Input sequence is empty")
        self.scores = scores

    def calculate_mean(self):
        return sum(self.scores) / len(self.scores)

if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92)
    calculator = ScoreCalculator(sample_scores)
    mean = calculator.calculate_mean()
    print(mean)