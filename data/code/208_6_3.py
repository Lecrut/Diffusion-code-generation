class DataAnalyzer:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of numbers")
        self.data = data
    
    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count

if __name__ == '__main__':
    analyzer = DataAnalyzer([10, 20, 30, 40])
    print(analyzer.calculate_mean())