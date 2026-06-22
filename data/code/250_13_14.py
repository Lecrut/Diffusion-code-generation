class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([10.5, 20.5, 30.5])
    print(f"Data: {analyzer1.data}, Mean: {analyzer1.calculate_mean()}")

    analyzer2 = DataAnalyzer([1.0, 2.0, 3.0, 4.0, 5.0])
    print(f"Data: {analyzer2.data}, Mean: {analyzer2.calculate_mean()}")

    analyzer3 = DataAnalyzer([100.0, 50.5, 75.25])
    print(f"Data: {analyzer3.data}, Mean: {analyzer3.calculate_mean()}")

    analyzer4 = DataAnalyzer([3.14, 2.71, 1.618])
    print(f"Data: {analyzer4.data}, Mean: {analyzer4.calculate_mean()}")