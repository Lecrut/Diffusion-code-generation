class DataCalculator:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of numbers")
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    calculator = DataCalculator([12, 24, 36, 48])
    print(calculator.calculate_mean())