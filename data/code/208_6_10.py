class DataCalculator:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of numbers")
        self.data = data

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

if __name__ == '__main__':
    calculator = DataCalculator([10, 20, 30, 40])
    print(calculator.calculate_mean())