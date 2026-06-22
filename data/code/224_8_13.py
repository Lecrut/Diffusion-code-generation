class ScoreCalculator:
    def __init__(self, scores):
        self.scores = scores
    
    def calculate_mean(self):
        return sum(self.scores) / len(self.scores)

if __name__ == '__main__':
    calculator = ScoreCalculator([85, 90, 78, 92, 88])
    print(calculator.calculate_mean())