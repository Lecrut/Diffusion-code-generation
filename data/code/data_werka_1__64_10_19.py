def find_final_index(indices):
    if not indices:
        return None
    last_index = len(indices) - 1
    return indices[last_index]

if __name__ == '__main__':
    sample_indices = [10, 20, 30, 40, 50]
    final_index = find_final_index(sample_indices)
    print(final_index)