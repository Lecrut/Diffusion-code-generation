def validate_indices(indices):
    if not isinstance(indices, list):
        raise ValueError("Input must be a list")
    for index in indices:
        if not isinstance(index, int):
            raise ValueError("All elements in the list must be integers")

def find_final_index(indices):
    validate_indices(indices)
    if not indices:
        return -1
    return indices[-1]

if __name__ == '__main__':
    sample_indices = [7, 3, 9, 2, 6]
    final_index = find_final_index(sample_indices)
    print(final_index)