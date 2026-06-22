import itertools

def flatten_list(nested_lists):
    if not all(isinstance(sublist, list) for sublist in nested_lists):
        raise ValueError("All elements of the input must be lists.")
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample = [[1, 2, 3], [4, 5], [6]]
    print(flatten_list(sample))