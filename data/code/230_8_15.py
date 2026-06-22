import itertools

def flatten_nested_list(nested_lists):
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2, 3], [4, 5], [6]]
    flattened_data = flatten_nested_list(sample_data)
    print(flattened_data)