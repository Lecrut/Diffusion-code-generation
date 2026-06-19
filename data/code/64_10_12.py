def find_final_index(indices):
    if not isinstance(indices, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the list must be integers.")
    if not indices:
        return -1
    return indices[-1]

if __name__ == '__main__':
    sample_indices = [10, 20, 30, 40, 50]
    try:
        final_index = find_final_index(sample_indices)
        print(final_index)
    except (TypeError, ValueError) as e:
        print(e)