import numpy as np

class DataAnalyzer:
    @staticmethod
    def calculate_average(data):
        return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    analyzer = DataAnalyzer()
    average = analyzer.calculate_average(sample_data)
    print(f"Average of {sample_data}: {average}")