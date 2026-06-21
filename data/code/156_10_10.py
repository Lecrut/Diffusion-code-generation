import statistics

class AverageCalculator:
    DEFAULT_VALUE = 0
    
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return AverageCalculator.DEFAULT_VALUE
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    mean1 = calculator.calculate_mean(sample_list)
    mean2 = calculator.calculate_mean(empty_list)
    print(f"Mean of {sample_list}: {mean1}")
    print(f"Mean of {empty_list}: {mean2}")