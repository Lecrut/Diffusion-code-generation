class TupleFilter:
    def __init__(self, tuples):
        self.tuples = tuples

    def filter_by_criteria(self, min_value, max_length):
        return [t for t in self.tuples if min_value <= sum(t) <= max_value and len(t) <= max_length]

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
    filter_instance = TupleFilter(sample_tuples)
    filtered_tuples = filter_instance.filter_by_criteria(5, 3)
    print(filtered_tuples)