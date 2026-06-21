import numpy as np

class AverageCalculator:
    @staticmethod
    def calculate_average(data):
        return np.mean(data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data1 = [1, 2, 3, 4, 5]
    sample_data2 = [10, 20, 30, 40, 50]
    print(f"Average of {sample_data1}: {calculator.calculate_average(sample_data1)}")
    print(f"Average of {sample_data2}: {calculator.calculate_average(sample_data2)}")