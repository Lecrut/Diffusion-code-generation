import statistics

class ScoreCalculator:
    @staticmethod
    def calculate_mean(scores):
        if not scores:
            return 0
        return statistics.mean(scores)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    test_scores1 = [1, 2, 3, 4, 5]
    test_scores2 = []
    test_scores3 = [10.5, 20.5, 30.5]
    test_scores4 = [-1, 5, 10, -5]
    
    print(f"Mean of {test_scores1}: {calculator.calculate_mean(test_scores1)}")
    print(f"Mean of {test_scores2}: {calculator.calculate_mean(test_scores2)}")
    print(f"Mean of {test_scores3}: {calculator.calculate_mean(test_scores3)}")
    print(f"Mean of {test_scores4}: {calculator.calculate_mean(test_scores4)}")