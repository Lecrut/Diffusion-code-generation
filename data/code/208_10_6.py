import statistics

class MeanCalculator:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return None
        return statistics.mean(numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_values = [10, 20, 30, 40, 50]
    empty_list = []
    print(f"Mean of {sample_values}: {calculator.calculate_mean(sample_values)}")
    print(f"Mean of {empty_list}: {calculator.calculate_mean(empty_list)}")