import statistics

class ScoreAnalyzer:
    SAMPLE_SCORES = [85, 92, 78, 90, 88, 76, 95, 89, 91, 84]

    @staticmethod
    def compute_mean(values):
        return statistics.mean(values)

    @classmethod
    def get_sample_mean(cls):
        return cls.compute_mean(cls.SAMPLE_SCORES)

def analyze_scores(scores):
    return ScoreAnalyzer.compute_mean(scores)

if __name__ == '__main__':
    test_data = ScoreAnalyzer.SAMPLE_SCORES
    mean_value = analyze_scores(test_data)
    print(mean_value)