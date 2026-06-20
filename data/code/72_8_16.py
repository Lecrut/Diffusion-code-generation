def compare_elements(data, indices):
    for idx1, idx2 in zip(indices, indices[1:]):
        if data[idx1] == data[idx2]:
            print(f"Elements at indices {idx1} and {idx2} are equal.")
        else:
            print(f"Elements at indices {idx1} and {idx2} are not equal.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 1, 3]
    compare_elements(sample_data, sample_indices)