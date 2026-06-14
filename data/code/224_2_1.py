class ScoreAnalyzer:
    def get_mean(self, scores):
        if not scores:
            return 0
        return sum(scores) / len(scores)
if __name__ == '__main__':
    analyzer = ScoreAnalyzer()
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = analyzer.get_mean(sample_scores)
    print(mean_score)