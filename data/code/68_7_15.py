class DifferenceCalculator:
    def __init__(self, list1: list[float], list2: list[float]):
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def calculate_difference(a: float, b: float) -> float:
        return abs(a - b)

    def get_differences(self) -> list[float]:
        differences = []
        for a in self.list1:
            for b in self.list2:
                diff = self.calculate_difference(a, b)
                differences.append(diff)
        return differences

if __name__ == '__main__':
    A_sample = [1.5, 3.7, 5.9]
    B_sample = [2.4, 6.8, 10.1]
    calculator = DifferenceCalculator(A_sample, B_sample)
    result = calculator.get_differences()
    print(result)