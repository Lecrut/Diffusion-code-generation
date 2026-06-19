from typing import List

class DifferenceCalculator:
    def __init__(self, list_a: List[float], list_b: List[float]):
        self.list_a = list_a
        self.list_b = list_b

    def calculate_differences(self) -> List[float]:
        differences = []
        for a in self.list_a:
            for b in self.list_b:
                difference = abs(a - b)
                differences.append(difference)
        return differences

if __name__ == '__main__':
    A_sample = [1.5, 3.2, 7.8]
    B_sample = [2.1, 4.5, 6.0]
    
    calculator = DifferenceCalculator(A_sample, B_sample)
    differences = calculator.calculate_differences()
    print(differences)