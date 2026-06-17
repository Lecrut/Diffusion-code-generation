def compare_adjacent(data):
    results = []
    n = len(data)
    for i in range(n - 1):
        a = data[i]
        b = data[i+1]
        results.append((a, b))
    return results
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    comparison_results = compare_adjacent(sample_list)
    print(comparison_results)