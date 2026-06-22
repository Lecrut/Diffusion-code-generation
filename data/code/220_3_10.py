class DataAnalyzer:
    def __init__(self, datasets):
        self.datasets = datasets

    def calculate_mean(self):
        total_sum = sum(sum(dataset) for dataset in self.datasets)
        total_count = sum(len(dataset) for dataset in self.datasets)
        return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    analyzer = DataAnalyzer([
        {1, 2},
        {3, 4, 5},
        {6}
    ])
    print(f"Mean of datasets: {analyzer.calculate_mean()}")