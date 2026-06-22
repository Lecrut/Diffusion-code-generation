class TestScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def get_count(self):
        return len(self.scores)

    def get_total(self):
        return sum(self.scores)

    def calculate_average(self):
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)

if __name__ == '__main__':
    STATIC_SCORES = [74, 82, 91, 68, 95, 89]
    analyzer = TestScoreAnalyzer(STATIC_SCORES)
    print(analyzer.calculate_average())
    print(analyzer.get_total())
    print(analyzer.get_count())