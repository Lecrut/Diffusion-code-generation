def find_final_index(indices):
    index_status = {
        'empty': -1,
        'non_empty': None
    }
    
    if not indices:
        return index_status['empty']
    
    return indices[-1]

if __name__ == '__main__':
    sample_indices = [7, 2, 9, 4, 6]
    final_index = find_final_index(sample_indices)
    print(final_index)