import itertools

class ListFlattener:
    @staticmethod
    def flatten(nested_lists):
        return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    flattened_list = ListFlattener.flatten(sample_data)
    print(flattened_list)