class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        mean = total / count if count > 0 else None
        return mean

if __name__ == '__main__':
    analyzer = DataAnalyzer([10, 20, 30, 40, 50])
    print(analyzer.calculate_mean())