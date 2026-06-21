import itertools

class ListFlattener:
    @staticmethod
    def flatten(nested_lists):
        return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    flattener = ListFlattener()
    result = flattener.flatten(sample_data)
    print(result)