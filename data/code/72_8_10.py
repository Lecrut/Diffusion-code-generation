def compare_elements(data, indices):
    for i in range(len(indices) - 1):
        if data[indices[i]] == data[indices[i + 1]]:
            print(f"Elements at indices {indices[i]} and {indices[i + 1]} are equal.")
        else:
            print(f"Elements at indices {indices[i]} and {indices[i + 1]} are not equal.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 1]
    compare_elements(sample_data, sample_indices)