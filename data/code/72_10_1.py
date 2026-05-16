def compare_data(data, indices):
    results = []
    for i1, i2 in indices:
        if 0 <= i1 < len(data) and 0 <= i2 < len(data):
            comparison = data[i1] == data[i2]
            results.append((i1, i2, comparison, data[i1], data[i2]))
        else:
            results.append((i1, i2, False, None, None))
    return results
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80]
    comparison_indices = [(0, 3), (1, 5), (2, 2), (4, 0), (7, 1)]
    comparison_results = compare_data(sample_data, comparison_indices)
    for i1, i2, match, val1, val2 in comparison_results:
        print(f"Comparing index {i1} ({sample_data[i1]}) with index {i2} ({sample_data[i2]}): Match = {match}")