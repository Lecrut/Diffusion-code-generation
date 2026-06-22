class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if not self.data:
            return 0
        total_sum = sum(sum(subset) for subset in self.data)
        total_count = sum(len(subset) for subset in self.data)
        return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([[1, 2], [3, 4, 5], [6]])
    print(f"Mean of data1: {analyzer1.calculate_mean()}")

    analyzer2 = DataAnalyzer([{1, 2}, {3, 4}])
    print(f"Mean of data2: {analyzer2.calculate_mean()}")

    analyzer3 = DataAnalyzer([set(), {10}])
    print(f"Mean of data3: {analyzer3.calculate_mean()}")