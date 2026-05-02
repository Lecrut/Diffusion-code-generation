def find_all_indices(data, item):
    indices = []
    for i, x in enumerate(data):
        if x == item:
            indices.append(i)
    return indices
def find_final_index(data, item):
    indices = find_all_indices(data, item)
    if not indices:
        return -1
    return indices[-1]
if __name__ == '__main__':
    sample_data = [1, 5, 2, 5, 8, 5, 3]
    target_item = 5
    final_index = find_final_index(sample_data, target_item)
    print(final_index)