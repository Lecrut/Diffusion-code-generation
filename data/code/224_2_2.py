class ScoreAnalyzer:
    def get_mean(self, scores):
        if not scores:
            return 0
        return sum(scores) / len(scores)
if __name__ == '__main__':
    analyzer = ScoreAnalyzer()
    sample_scores1 = [85, 90, 78, 88]
    mean1 = analyzer.get_mean(sample_scores1)
    print(f"Mean of {sample_scores1}: {mean1}")
    sample_scores2 = [10, 20, 30, 40, 50]
    mean2 = analyzer.get_mean(sample_scores2)
    print(f"Mean of {sample_scores2}: {mean2}")
    sample_scores3 = []
    mean3 = analyzer.get_mean(sample_scores3)
    print(f"Mean of {sample_scores3}: {mean3}")