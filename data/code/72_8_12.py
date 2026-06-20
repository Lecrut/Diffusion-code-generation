def compare_elements(data, indices):
    for index_pair in indices:
        if len(index_pair) != 2:
            raise ValueError("Each index pair must contain exactly two elements.")
        i, j = index_pair
        if i >= len(data) or j >= len(data):
            raise IndexError("Index out of range.")
        print(f"Comparing {data[i]} and {data[j]}: {'Equal' if data[i] == data[j] else 'Not Equal'}")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [(0, 2), (1, 3), (2, 4)]
    compare_elements(sample_data, sample_indices)