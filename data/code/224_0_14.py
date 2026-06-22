class ScoreCalculator:
    @staticmethod
    def calculate_mean(scores):
        if not scores:
            return None
        total = sum(scores)
        count = len(scores)
        return total / count

if __name__ == '__main__':
    calculator = ScoreCalculator()
    scores = [10, 20, 30, 40, 50]
    mean_score = calculator.calculate_mean(scores)
    print(mean_score)