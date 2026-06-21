import numpy as np

class DataAnalyzer:
    @staticmethod
    def calculate_median(data):
        if len(data) == 0:
            return None
        return np.median(data)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    print(analyzer.calculate_median([1, 5, 2, 8, 3]))
    print(analyzer.calculate_median([10, 20, 30, 40, 50, 60]))
    print(analyzer.calculate_median([7]))
    print(analyzer.calculate_median([]))