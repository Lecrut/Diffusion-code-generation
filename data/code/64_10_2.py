def find_final_index(indices):
    if not indices:
        return None
    return indices[-1]

if __name__ == '__main__':
    sample_indices = [0, 3, 5, 7, 9]
    final_index = find_final_index(sample_indices)
    print(final_index)