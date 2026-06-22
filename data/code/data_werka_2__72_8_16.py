def compare_elements(data, indices):
    results = []
    for i in range(len(indices) - 1):
        idx1 = indices[i]
        idx2 = indices[i + 1]
        if idx1 < 0 or idx1 >= len(data) or idx2 < 0 or idx2 >= len(data):
            raise ValueError(f"Index out of range: {idx1} or {idx2}")
        val1 = data[idx1]
        val2 = data[idx2]
        if val1 < val2:
            results.append(f"{val1} < {val2}")
        elif val1 > val2:
            results.append(f"{val1} > {val2}")
        else:
            results.append(f"{val1} == {val2}")
    return results

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    sample_indices = [0, 1, 2, 3, 4]
    result = compare_elements(sample_data, sample_indices)
    for res in result:
        print(res)