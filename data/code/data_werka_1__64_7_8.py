def find_all_indices(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    try:
        return next(i for i in reversed(list(find_all_indices(data, item))))
    except StopIteration:
        return -1

if __name__ == '__main__':
    sample_data = [10, 23, 56, 23, 87, 23, 45]
    target_item = 23
    final_index = find_final_index(sample_data, target_item)
    print(final_index)