def compare_consecutive_elements(data):
    comparison_results = {}
    n = len(data)
    for i in range(n - 1):
        element_pair = (data[i], data[i + 1])
        if element_pair[0] == element_pair[1]:
            comparison_status = "Equal"
        elif abs(element_pair[0] - element_pair[1]) < 1e-9:
            comparison_status = "Almost Equal"
        else:
            comparison_status = "Not Equal"
        comparison_results[element_pair] = comparison_status
    return comparison_results

if __name__ == '__main__':
    sample_data = [1.0, 1.0005, 2.0, 3.001, 5.0]
    result = compare_consecutive_elements(sample_data)
    for pair, status in result.items():
        print(f"Pair {pair}: {status}")