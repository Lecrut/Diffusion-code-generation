import statistics

class TestScoresCalculator:
    @staticmethod
    def calculate_mean(scores):
        return statistics.mean(scores)

if __name__ == '__main__':
    calculator = TestScoresCalculator()
    scores1 = [1, 2, 3, 4, 5]
    scores2 = []
    scores3 = [10.5, 20.5, 30.5]
    scores4 = [-1, 5, 10, -5]
    
    print(f"Mean of {scores1}: {calculator.calculate_mean(scores1)}")
    print(f"Mean of {scores2}: {calculator.calculate_mean(scores2)}")
    print(f"Mean of {scores3}: {calculator.calculate_mean(scores3)}")
    print(f"Mean of {scores4}: {calculator.calculate_mean(scores4)}")