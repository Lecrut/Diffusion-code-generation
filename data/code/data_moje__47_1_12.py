import statistics

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = list(scores)

    def mean(self):
        return statistics.mean(self.scores)

    def median(self):
        return statistics.median(self.scores)

    def count(self):
        return len(self.scores)

if __name__ == '__main__':
    raw_scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 84]
    analyzer = ScoreAnalyzer(raw_scores)
    print(analyzer.mean())
    print(analyzer.median())
    print(analyzer.count())