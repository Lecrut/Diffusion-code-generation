import math

class ScoreCalculator:
    def __init__(self, scores):
        self.scores = scores
    
    def calculate_mean(self):
        return math.fsum(self.scores) / len(self.scores)

if __name__ == '__main__':
    calculator = ScoreCalculator([10, 20, 30, 40, 50])
    mean_score = calculator.calculate_mean()
    print(mean_score)