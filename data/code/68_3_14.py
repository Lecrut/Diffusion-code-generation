class DifferenceCalculator:
    def __init__(self, list_a, list_b):
        if len(list_a) != len(list_b):
            raise ValueError("Lists A and B must be of the same length.")
        self.differences = [a - b for a, b in zip(list_a, list_b)]

    def get_differences(self):
        return self.differences

if __name__ == '__main__':
    A = [10, 20, 30]
    B = [5, 15, 25]
    calculator = DifferenceCalculator(A, B)
    print(calculator.get_differences())