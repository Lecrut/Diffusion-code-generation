import itertools

def flatten_nested_lists(nested_lists):
    if not isinstance(nested_lists, list):
        raise TypeError("Input must be a list")
    
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    print(flatten_nested_lists(sample_data))