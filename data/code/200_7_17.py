import itertools

def is_valid_nested_list(nested_lists):
    for element in nested_lists:
        if not isinstance(element, list):
            return False
    return True

def flatten_nested_lists(nested_lists):
    if not is_valid_nested_list(nested_lists):
        raise ValueError("Input must be a list of lists")
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    print(flatten_nested_lists(sample_data))