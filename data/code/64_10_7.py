def find_final_index(indices):
    index_status = {'found': None}
    if indices:
        index_status['found'] = indices[-1]
    return index_status.get('found', -1)

if __name__ == '__main__':
    sample_indices = [2, 7, 1, 4, 9]
    final_index = find_final_index(sample_indices)
    print(final_index)