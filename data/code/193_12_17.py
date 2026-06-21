class NumericAggregator:
    def __init__(self, data):
        self._data = data

    def aggregate(self):
        return sum(filter(lambda x: isinstance(x, (int, float)), self._data))

if __name__ == '__main__':
    sample_data = [10, 'a', 25.5, None, 30, 5, 'b']
    aggregator = NumericAggregator(sample_data)
    total = aggregator.aggregate()
    print(total)