def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    final_index = find_final_index(sample_list)
    print(final_index)