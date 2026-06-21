from typing import List

class DataAnalyzer:
    def __init__(self, data: List[float]):
        self.data = data

    def calculate_average(self) -> float:
        if not self.data:
            return 0.0
        total = sum(self.data)
        count = len(self.data)
        average = total / count
        return average

if __name__ == '__main__':
    sample_data = [30, 40, 50, 60, 70]
    analyzer = DataAnalyzer(sample_data)
    print(analyzer.calculate_average())