def compare_elements(data, indices):
    if not indices:
        return []
    results = []
    for i in range(len(indices) - 1):
        current_idx = indices[i]
        next_idx = indices[i + 1]
        if not (0 <= current_idx < len(data)):
            raise ValueError(f"Index {current_idx} out of range")
        if not (0 <= next_idx < len(data)):
            raise ValueError(f"Index {next_idx} out of range")
        first_value = data[current_idx]
        second_value = data[next_idx]
        if first_value < second_value:
            comparison_str = f"{first_value} < {second_value}"
        elif first_value > second_value:
            comparison_str = f"{first_value} > {second_value}"
        else:
            comparison_str = f"{first_value} == {second_value}"
        results.append(comparison_str)
    return results

if __name__ == '__main__':
    dataset = [5, 10, 3, 8, 12, 1]
    target_indices = [0, 2, 4]
    output = compare_elements(dataset, target_indices)
    print(output)