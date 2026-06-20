def compare_elements(data_list, indices):
    for i in range(len(indices) - 1):
        print(f"Comparing elements at indices {indices[i]} and {indices[i + 1]}:")
        if data_list[indices[i]] == data_list[indices[i + 1]]:
            print("Elements are equal.")
        else:
            print("Elements are not equal.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 3, 4]
    compare_elements(sample_data, sample_indices)