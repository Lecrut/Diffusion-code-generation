from typing import List

class AverageCalculator:
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
    sample_data = [15, 25, 35, 45, 55]
    calculator = AverageCalculator(sample_data)
    print(calculator.calculate_average())