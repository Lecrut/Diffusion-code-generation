def compare_consecutive_elements(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")
    if len(data) < 2:
        raise ValueError("Input tuple must contain at least two elements")

    comparison_results = {}
    n = len(data)
    for i in range(n - 1):
        comparison_results[(data[i], data[i+1])] = "Equal" if data[i] == data[i+1] else "Not Equal"

    return comparison_results

if __name__ == '__main__':
    sample_data = (1.0, 1.0005, 2.0, 2.001, 3.0, 3.0001)
    result = compare_consecutive_elements(sample_data)
    for pair, status in result.items():
        print(f"Pair {pair}: {status}")