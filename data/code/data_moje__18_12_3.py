def find_median_index(values):
    if not values:
        raise ValueError("List cannot be empty")
    n = len(values)
    indices = list(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if values[indices[i]] > values[indices[j]]:
                indices[i], indices[j] = indices[j], indices[i]
    median_pos = n // 2
    if n % 2 == 1:
        return indices[median_pos]
    else:
        idx1 = indices[median_pos - 1]
        idx2 = indices[median_pos]
        val1 = values[idx1]
        val2 = values[idx2]
        if idx1 < idx2:
            return (idx1 + idx2) // 2
        else:
            return (idx2 + idx1) // 2

if __name__ == '__main__':
    sample_data = [10, 20, 5, 15, 25]
    result = find_median_index(sample_data)
    print(result)