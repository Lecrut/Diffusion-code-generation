def compare_adjacent(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the list must be numbers.")
    
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i + 1]
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