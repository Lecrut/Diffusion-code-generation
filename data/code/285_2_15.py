def compare_consecutive_elements(data):
    comparisons = {}
    n = len(data)
    for i in range(n - 1):
        if data[i] != data[i+1]:
            comparisons[(data[i], data[i+1])] = "Different"
        else:
            comparisons[(data[i], data[i+1])] = "Same"
    return comparisons

if __name__ == '__main__':
    sample_data = (1, 2, 3, 4, 5)
    result = compare_consecutive_elements(sample_data)
    for pair, status in result.items():
        print(f"Pair: {pair}, Status: {status}")