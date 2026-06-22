def max_adjacent_pairs(data):
    results = []
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            results.append(data[i])
        else:
            results.append(data[i + 1])
    return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3, 0]
    comparison_results = max_adjacent_pairs(sample_data)
    print(comparison_results)