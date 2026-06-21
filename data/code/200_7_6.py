import itertools

def validate_input(nested_lists):
    if not all(isinstance(item, (list, int)) for item in nested_lists):
        raise ValueError("Input must be a list of integers and/or lists")

def flatten_nested_lists(nested_lists):
    validate_input(nested_lists)
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    print(flatten_nested_lists(sample_data))