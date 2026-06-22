def find_final_index(indices):
    index_status = {'has_indices': False, 'final_index': -1}
    if indices:
        index_status['has_indices'] = True
        index_status['final_index'] = indices[-1]
    return index_status['final_index']

if __name__ == '__main__':
    sample_indices = [7, 2, 9, 4, 6]
    final_index = find_final_index(sample_indices)
    print(final_index)