def validate_input(data):
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Input must be a non-empty list with at least two elements")

def compare_adjacent(data):
    validate_input(data)
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if a > b:
            results.append("increasing")
        elif a < b:
            results.append("decreasing")
        else:
            results.append("equal")
    return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = compare_adjacent(sample_data)
    print(comparison_results)