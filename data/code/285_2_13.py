def compare_consecutive_elements(data):
    comparison_results = {}
    n = len(data)
    for i in range(n - 1):
        element_pair = (data[i], data[i+1])
        comparison_status = "Equal" if data[i] == data[i+1] else "Different"
        comparison_results[element_pair] = comparison_status
    return comparison_results

if __name__ == '__main__':
    sample_data = (1.0, 2.0, 3.0, 4.0, 5.0)
    result = compare_consecutive_elements(sample_data)
    for pair, status in result.items():
        print(f"Pair: {pair}, Status: {status}")