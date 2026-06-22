def validate_indices(indices):
    if not isinstance(indices, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the list must be integers.")

def find_final_index(indices):
    validate_indices(indices)
    return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_indices = [7, 2, 9, 4, 6]
    final_index = find_final_index(sample_indices)
    print(final_index)