class MaxDifferenceCalculator:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def find_min_max(self, lst):
        if not lst:
            return 0, 0
        return min(lst), max(lst)

    def calculate_max_difference(self):
        min_a, max_a = self.find_min_max(self.list_a)
        min_b, max_b = self.find_min_max(self.list_b)
        return max(max_a - min_b, max_b - min_a)

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    calculator = MaxDifferenceCalculator(list_a, list_b)
    print(calculator.calculate_max_difference())