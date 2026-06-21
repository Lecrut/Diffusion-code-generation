import itertools

def flatten_nested_lists(nested_lists):
    if not all(isinstance(sublist, list) for sublist in nested_lists):
        raise ValueError("All elements must be lists")
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    flattened_list = flatten_nested_lists(sample_data)
    print(flattened_list)