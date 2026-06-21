import numpy as np

class AverageCalculator:
    def calculate_average(self, data):
        if not data:
            return 0
        return np.mean(data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data1 = [1.0, 2.5, 3.5, 4.0]
    sample_data2 = [10, 20, 30, 40, 50]
    sample_data3 = []
    sample_data4 = [7.0]
    print(f"Average of {sample_data1}: {calculator.calculate_average(sample_data1)}")
    print(f"Average of {sample_data2}: {calculator.calculate_average(sample_data2)}")
    print(f"Average of {sample_data3}: {calculator.calculate_average(sample_data3)}")
    print(f"Average of {sample_data4}: {calculator.calculate_average(sample_data4)}")