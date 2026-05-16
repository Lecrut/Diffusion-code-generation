def find_all_indices(data, item):
    indices = []
    for i, x in enumerate(data):
        if x == item:
            indices.append(i)
    return indices
if __name__ == '__main__':
    sample_data = [1, 5, 2, 5, 8, 5, 3]
    target_item = 5
    all_indices = find_all_indices(sample_data, target_item)
    if all_indices:
        final_index = all_indices[-1]
        print(final_index)
    else:
        print(f"{target_item} not found in the list.")