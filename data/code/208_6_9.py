class DataCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if not self.data:
            return None
        total = sum(self.data)
        count = len(self.data)
        return total / count

if __name__ == '__main__':
    calculator1 = DataCalculator([10, 20, 30, 40])
    print(calculator1.calculate_mean())

    calculator2 = DataCalculator([5, 15, 25, 35, 45])
    print(calculator2.calculate_mean())