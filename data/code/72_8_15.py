def compare_elements(data, indices):
    for i, j in indices:
        if data[i] == data[j]:
            print(f"Elements at indices {i} and {j} are equal: {data[i]}")
        else:
            print(f"Elements at indices {i} and {j} are not equal: {data[i]} != {data[j]}")

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    indices = [(0, 2), (1, 3), (2, 4)]
    compare_elements(data, indices)