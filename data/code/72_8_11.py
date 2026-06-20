def compare_elements(data, indices):
    for i in range(len(indices) - 1):
        if data[indices[i]] == data[indices[i + 1]]:
            print(f"Element at index {indices[i]} is equal to element at index {indices[i + 1]}")
        else:
            print(f"Element at index {indices[i]} is not equal to element at index {indices[i + 1]}")

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    indices = [0, 2, 4, 1]
    compare_elements(data, indices)