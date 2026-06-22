def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        current = data[i]
        next_value = data[i + 1]
        if current > next_value:
            results.append("decreasing")
        elif current < next_value:
            results.append("increasing")
        else:
            results.append("equal")
    return results

if __name__ == '__main__':
    sample_data = [4, 2, 3, 7, 7, 5]
    comparison_results = compare_adjacent(sample_data)
    print(comparison_results)