import itertools

def flatten_nested_lists(nested_lists):
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[10, 20], [30, 40], [50, 60]]
    flattened_list = flatten_nested_lists(sample_data)
    print(flattened_list)