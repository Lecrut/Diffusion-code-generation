from functools import reduce

class NumberAggregator:
    @staticmethod
    def aggregate(numbers):
        return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 7, 9]
    aggregator_instance = NumberAggregator()
    total_sum = aggregator_instance.aggregate(sample_values)
    print(total_sum)