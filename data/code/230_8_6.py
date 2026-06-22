import itertools

def validate_input(nested_list):
    if not all(isinstance(sublist, list) for sublist in nested_list):
        raise ValueError("All elements must be lists")

def flatten_list(nested_list):
    validate_input(nested_list)
    return list(itertools.chain.from_iterable(nested_list))

if __name__ == '__main__':
    sample = [[1, 2], [3, 4], [5, 6]]
    print(flatten_list(sample))