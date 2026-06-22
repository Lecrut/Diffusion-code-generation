def compare_adjacent(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")
    
    results = []
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
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