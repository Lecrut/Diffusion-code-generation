import itertools

class ListFlattener:
    def flatten(self, nested_lists):
        return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    flattener = ListFlattener()
    sample_data = [[1, 2, 3], [4, 5], [6]]
    flattened_result = flattener.flatten(sample_data)
    print(flattened_result)