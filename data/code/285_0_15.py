COMPARISON_INCREASING = "increasing"
COMPARISON_DECREASING = "decreasing"
COMPARISON_EQUAL = "equal"

def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if a > b:
            results.append(COMPARISON_DECREASING)
        elif a < b:
            results.append(COMPARISON_INCREASING)
        else:
            results.append(COMPARISON_EQUAL)
    return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = compare_adjacent(sample_data)
    print(comparison_results)