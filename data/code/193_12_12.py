class NumericAggregator:
    def __init__(self, data):
        self._data = data
    
    def sum_values(self):
        return sum(filter(lambda x: isinstance(x, (int, float)), self._data))

if __name__ == '__main__':
    sample_list = [10, 'a', 25.3, 30, None, 5]
    aggregator = NumericAggregator(sample_list)
    total_sum = aggregator.sum_values()
    print(total_sum)