def compare_elements(data_list, indices):
    for i, j in indices:
        if data_list[i] == data_list[j]:
            print(f"Elements at index {i} and {j} are equal.")
        else:
            print(f"Elements at index {i} and {j} are not equal.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [(0, 2), (1, 3), (2, 4)]
    compare_elements(sample_data, sample_indices)