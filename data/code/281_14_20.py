class NumberAggregator:
    def __init__(self):
        self.numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    def get_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    aggregator = NumberAggregator()
    print(aggregator.get_sum())