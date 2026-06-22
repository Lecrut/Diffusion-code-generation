import numpy as np

class AverageCalculator:
    @staticmethod
    def calculate_single_average(numbers):
        if numbers:
            return np.mean(numbers)
        return 0

    @classmethod
    def calculate_all_averages(cls, list_of_lists):
        return [cls.calculate_single_average(inner_list) for inner_list in list_of_lists]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5]
    ]
    calculator = AverageCalculator()
    result = calculator.calculate_all_averages(sample_data)
    print(result)