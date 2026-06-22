def find_all_indices(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def get_final_index(indices):
    return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_data = [4, 9, 2, 4, 8, 4, 6]
    target_item = 4
    index_generator = find_all_indices(sample_data, target_item)
    all_indices = list(index_generator)
    final_index = get_final_index(all_indices)
    print(final_index)