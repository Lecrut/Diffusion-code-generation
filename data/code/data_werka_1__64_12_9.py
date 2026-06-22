def find_final_index(indices):
    if not indices:
        return -1
    return indices[-1]
if __name__ == '__main__':
    sample_indices = [0, 3, 5, 7]
    empty_indices = []
    print(find_final_index(sample_indices))
    print(find_final_index(empty_indices))