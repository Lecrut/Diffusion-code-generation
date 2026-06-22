def compare_adjacent_elements(sequence):
    COMPARISON_RESULTS = ['increasing', 'decreasing', 'equal']
    comparison_results = []
    n = len(sequence)
    for i in range(n - 1):
        a, b = sequence[i], sequence[i + 1]
        if a > b:
            result = COMPARISON_RESULTS[0]
        elif a < b:
            result = COMPARISON_RESULTS[1]
        else:
            result = COMPARISON_RESULTS[2]
        comparison_results.append(result)
    return comparison_results

if __name__ == '__main__':
    sample_data = [10, 5, 5, 20, 30]
    print(compare_adjacent_elements(sample_data))