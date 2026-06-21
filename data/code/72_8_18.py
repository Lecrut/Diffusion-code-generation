def compare_elements(data, indices):
    results = []
    for i in indices:
        if i < 0 or i >= len(data):
            raise ValueError(f"Index {i} is out of range for data of length {len(data)}")
        if i + 1 >= len(data):
            raise ValueError(f"Index {i} + 1 is out of range for data of length {len(data)}")
        val1 = data[i]
        val2 = data[i + 1]
        if val1 < val2:
            results.append(f"{val1} < {val2}")
        elif val1 > val2:
            results.append(f"{val1} > {val2}")
        else:
            results.append(f"{val1} == {val2}")
    return results

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    sample_indices = [0, 1, 2]
    output = compare_elements(sample_data, sample_indices)
    print(output)