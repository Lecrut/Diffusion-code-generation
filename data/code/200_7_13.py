import itertools

class ListFlattener:
    @staticmethod
    def flatten_nested_lists(nested_lists):
        return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    flattener = ListFlattener()
    print(flattener.flatten_nested_lists(sample_data))