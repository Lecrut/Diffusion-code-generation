from typing import List

class DifferenceCalculator:
    def __init__(self, list1: List[float], list2: List[float]):
        self.list1 = list1
        self.list2 = list2

    def calculate_differences(self) -> List[float]:
        return [a - b for a, b in zip(self.list1, self.list2)]

if __name__ == '__main__':
    sample_list1 = [6.0, 7.5, 8.9]
    sample_list2 = [2.3, 3.6, 4.8]
    calculator = DifferenceCalculator(sample_list1, sample_list2)
    differences = calculator.calculate_differences()
    print(differences)