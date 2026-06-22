class ScoreCalculator:
    @staticmethod
    def calculate_mean(scores):
        total = sum(scores)
        count = len(scores)
        mean = total / count
        return mean

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = ScoreCalculator.calculate_mean(sample_scores)
    print(result)