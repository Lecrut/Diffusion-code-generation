import itertools

def flatten_nested_lists(nested_lists):
    flattened = list(itertools.chain.from_iterable(nested_lists))
    return flattened

if __name__ == '__main__':
    sample_data = [[1, 2, [3]], 4, [5, 6], 7]
    result = flatten_nested_lists(sample_data)
    print(result)