def calculate_mean(scores):
    return sum(scores) / len(scores)

class ScoreCalculator:
    def __init__(self, scores):
        self.scores = scores
    
    def get_scores(self):
        return self.scores
    
    def set_scores(self, new_scores):
        self.scores = new_scores
    
    def calculate_mean(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

if __name__ == '__main__':
    calculator = ScoreCalculator([85, 90, 78, 92, 88])
    print("Original scores:", calculator.get_scores())
    new_scores = [80, 95, 83, 94, 86]
    calculator.set_scores(new_scores)
    print("Updated scores:", calculator.get_scores())
    print("Mean of updated scores:", calculator.calculate_mean())