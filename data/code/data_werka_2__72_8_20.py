COMPARISON_SYMBOLS = {
    -1: '<',
    0: '==',
    1: '>',
}

def compare_pair(data, i, j):
    if i < 0 or i >= len(data):
        raise ValueError(f"Index {i} out of range")
    if j < 0 or j >= len(data):
        raise ValueError(f"Index {j} out of range")
    val_i = data[i]
    val_j = data[j]
    if val_i < val_j:
        cmp = -1
    elif val_i > val_j:
        cmp = 1
    else:
        cmp = 0
    symbol = COMPARISON_SYMBOLS.get(cmp, '=')
    return f"{val_i} {symbol} {val_j}"

def compare_elements(data, indices):
    results = []
    n = len(indices)
    k = 1
    while k < n:
        idx1 = indices[k - 1]
        idx2 = indices[k]
        comparison_str = compare_pair(data, idx1, idx2)
        results.append(comparison_str)
        k += 1
    return results

if __name__ == '__main__':
    sample_data = [50, 10, 40, 20, 30]
    sample_indices = [0, 1, 2, 3]
    output = compare_elements(sample_data, sample_indices)
    print(output)