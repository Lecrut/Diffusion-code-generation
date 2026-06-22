import itertools

def flatten_list(nested_lists):
    return list(itertools.chain.from_iterable(nested_lists))

if __name__ == '__main__':
    sample_data = [[7, 8], [9, 10, 11], [12]]
    flattened_result = flatten_list(sample_data)
    print(flattened_result)