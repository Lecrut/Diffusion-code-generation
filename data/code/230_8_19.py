import itertools

def flatten_list(nested_lists):
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_values = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(flatten_list(sample_values))