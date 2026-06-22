def compare_first_greater(list_a, list_b):
    if not list_a or not list_b:
        return []
    results = []
    limit = min(len(list_a), len(list_b))
    for idx in range(limit):
        val_a = list_a[idx]
        val_b = list_b[idx]
        if val_a > val_b:
            results.append((val_a, val_b))
    return results

if __name__ == '__main__':
    sample_a = [15, 10, 20, 5]
    sample_b = [12, 12, 18, 6]
    output = compare_first_greater(sample_a, sample_b)
    for first, second in output:
        print(f"{first} > {second}")