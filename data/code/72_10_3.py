def compare_data(data, indices):
    results = []
    for i1, i2 in indices:
        if 0 <= i1 < len(data) and 0 <= i2 < len(data):
            result = data[i1] == data[i2]
            results.append((i1, i2, result))
        else:
            results.append((i1, i2, "Index out of bounds"))
    return results
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80]
    comparison_indices = [(0, 3), (1, 5), (2, 2), (4, 0), (7, 1)]
    comparison_results = compare_data(sample_data, comparison_indices)
    for i1, i2, result in comparison_results:
        if result is True:
            print(f"Data at index {i1} ({sample_data[i1]}) equals data at index {i2} ({sample_data[i2]}).")
        elif result == "Index out of bounds":
            print(f"Comparison between index {i1} and {i2}: Index out of bounds.")
        else:
            print(f"Data at index {i1} ({sample_data[i1]}) does not equal data at index {i2} ({sample_data[i2]}).")