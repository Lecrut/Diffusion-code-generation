class MaxDifferenceCalculator:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def calculate_max_difference(self):
        if not self.list_a or not self.list_b:
            return 0
        min_a = min(self.list_a)
        max_a = max(self.list_a)
        min_b = min(self.list_b)
        max_b = max(self.list_b)
        return max(max_a - min_b, max_b - min_a)

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    calculator = MaxDifferenceCalculator(list_a, list_b)
    print(calculator.calculate_max_difference())