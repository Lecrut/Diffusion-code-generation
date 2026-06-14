class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores
    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    analyzer = ScoreAnalyzer(sample_scores)
    average = analyzer.get_average()
    print(average)