class DataAggregator:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of numbers")
        self.data = data
    
    def compute_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    aggregator = DataAggregator([12, 34, 56, 78])
    print(aggregator.compute_mean())