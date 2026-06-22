def find_final_index(indices):
    index_map = {0: None}
    if indices:
        index_map[1] = indices[-1]
    return index_map.get(1, -1)

if __name__ == '__main__':
    sample_indices = [4, 6, 8, 10, 12]
    final_index = find_final_index(sample_indices)
    print(final_index)