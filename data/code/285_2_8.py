def compare_consecutive_pairs(data):
    comparison_results = {}
    n = len(data)
    for i in range(n - 1):
        pair = (data[i], data[i + 1])
        if data[i] == data[i + 1]:
            status = "Equal"
        elif data[i] < data[i + 1]:
            status = "Increasing"
        else:
            status = "Decreasing"
        comparison_results[pair] = status
    return comparison_results

if __name__ == '__main__':
    sample_data = (10, 20, 20, 30, 40)
    result = compare_consecutive_pairs(sample_data)
    print(result)