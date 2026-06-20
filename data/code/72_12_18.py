def find_inequality_indices(data):
    unequal_pairs = []
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            unequal_pairs.append((i, data[i], data[i + 1]))
    return unequal_pairs

if __name__ == '__main__':
    sample_data = [10, "apple", [20, 30], {"a": 40}, 5.5]
    print(find_inequality_indices(sample_data))