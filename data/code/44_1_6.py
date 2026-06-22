class ScoreAnalyzer:
    EMPTY_MEAN = 0.0

    @staticmethod
    def compute_mean(scores):
        if not scores:
            return ScoreAnalyzer.EMPTY_MEAN
        total = sum(scores)
        count = len(scores)
        return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    analyzer = ScoreAnalyzer()
    result = analyzer.compute_mean(test_scores)
    print(result)