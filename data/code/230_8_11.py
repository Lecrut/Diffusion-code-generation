import itertools

def flatten_list_of_lists(nested_list):
    return list(itertools.chain.from_iterable(nested_list))

if __name__ == '__main__':
    sample_data = [[1, 2, 3], [4, 5], [6]]
    print(flatten_list_of_lists(sample_data))