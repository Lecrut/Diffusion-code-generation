def is_valid_index_list(indices):
    return isinstance(indices, list) and all(isinstance(i, int) for i in indices)

def find_final_index(indices):
    if not is_valid_index_list(indices):
        raise ValueError("Input must be a list of integers.")
    if not indices:
        return -1
    return indices[-1]

if __name__ == '__main__':
    sample_indices = [7, 2, 9, 4, 6]
    try:
        final_index = find_final_index(sample_indices)
        print(final_index)
    except ValueError as e:
        print(e)