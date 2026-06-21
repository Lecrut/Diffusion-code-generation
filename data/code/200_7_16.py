import itertools

def flatten_nested_lists(nested_lists):
    flat_list = []
    for sublist in nested_lists:
        flat_list.extend(sublist)
    return list(itertools.chain.from_iterable(flat_list))

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    result = flatten_nested_lists(sample_data)
    print(result)