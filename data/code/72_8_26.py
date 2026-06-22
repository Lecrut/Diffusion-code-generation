def compare_indices(data, indices):
    if not indices:
        return []
    results = []
    for i in range(len(indices) - 1):
        idx_a = indices[i]
        idx_b = indices[i + 1]
        if not (-len(data) <= idx_a < len(data)):
            raise ValueError(f"Index {idx_a} out of range")
        if not (-len(data) <= idx_b < len(data)):
            raise ValueError(f"Index {idx_b} out of range")
        val_a = data[idx_a]
        val_b = data[idx_b]
        if val_a < val_b:
            results.append(f"{val_a} < {val_b}")
        elif val_a > val_b:
            results.append(f"{val_a} > {val_b}")
        else:
            results.append(f"{val_a} == {val_b}")
    return results

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    sample_indices = [0, 1, 2, 3]
    output = compare_indices(sample_data, sample_indices)
    print(output)