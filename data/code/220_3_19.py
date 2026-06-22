class DataAnalyzer:
    def __init__(self, datasets):
        self.datasets = datasets

    @staticmethod
    def calculate_mean(data):
        total_sum = sum(sum(dataset) for dataset in data)
        total_count = sum(len(dataset) for dataset in data)
        return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    analyzer = DataAnalyzer([
        {1, 2},
        {3, 4, 5},
        {6}
    ])
    print(f"Mean: {analyzer.calculate_mean(analyzer.datasets)}")