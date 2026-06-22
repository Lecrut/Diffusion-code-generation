class MinMaxCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_min_max(self):
        return min(self.data), max(self.data)

if __name__ == '__main__':
    sample_tuple = (15, 3, 8, 22, 1, 45, 9)
    calculator = MinMaxCalculator(sample_tuple)
    minimum, maximum = calculator.calculate_min_max()
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")