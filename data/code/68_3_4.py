class DifferenceCalculator:
    def __init__(self, list_a, list_b):
        if len(list_a) != len(list_b):
            raise ValueError("Lists A and B must be of the same length.")
        self.list_a = list_a
        self.list_b = list_b

    def calculate_differences(self):
        return [a - b for a, b in zip(self.list_a, self.list_b)]

if __name__ == '__main__':
    A = [20, 30, 40]
    B = [10, 15, 20]
    calculator = DifferenceCalculator(A, B)
    print(calculator.calculate_differences())