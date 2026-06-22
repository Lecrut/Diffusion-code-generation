class MinMaxCalculator:
    def __init__(self, data):
        self.data = data

    def compute_min_max(self):
        return min(self.data), max(self.data)

if __name__ == '__main__':
    calculator = MinMaxCalculator((15, 3, 8, 22, 1, 45, 9))
    minimum, maximum = calculator.compute_min_max()
    print(f"Sample Tuple: {calculator.data}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")