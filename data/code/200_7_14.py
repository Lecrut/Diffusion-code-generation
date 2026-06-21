import itertools

def flatten_nested_lists(nested_lists):
    if not all(isinstance(item, (list, tuple)) for item in nested_lists):
        raise ValueError("All elements must be lists or tuples")
    
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    print(flatten_nested_lists(sample_data))