class ScoreCalculator:
    def __init__(self, scores):
        self.scores = scores

    def calculate_mean(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

if __name__ == '__main__':
    calculator1 = ScoreCalculator([10, 20, 30, 40, 50])
    print(calculator1.calculate_mean())

    calculator2 = ScoreCalculator([])
    print(calculator2.calculate_mean())