def find_all_indices(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    indices = list(find_all_indices(data, item))
    if not indices:
        return -1
    return indices[-1]

if __name__ == '__main__':
    sample_data = [4, 7, 2, 7, 9, 7, 6]
    target_item = 7
    final_index = find_final_index(sample_data, target_item)
    print(final_index)