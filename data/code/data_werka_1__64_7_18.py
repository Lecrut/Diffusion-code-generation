def find_all_indices(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    try:
        return next(find_all_indices(reversed(data), item))
    except StopIteration:
        return -1

if __name__ == '__main__':
    sample_data = [1, 5, 2, 5, 8, 5, 3]
    target_item = 5
    final_index = find_final_index(sample_data, target_item)
    print(final_index)