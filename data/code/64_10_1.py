import sys
def find_final_index(indices):
    if not indices:
        return None
    return indices[-1]
if __name__ == '__main__':
    sample_indices = [1, 5, 2, 8, 3]
    final_index = find_final_index(sample_indices)
    print(final_index)