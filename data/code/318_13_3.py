def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        try:
            if a == b:
                results.append((i, a, b, "Equal"))
            else:
                results.append((i, a, b, "Not Equal"))
        except TypeError as e:
            print(f"Error comparing elements at indices {i} and {i+1}: {e}")
            results.append((i, a, b, "Type Error"))
    return results
if __name__ == '__main__':
    sample_data = [10, "20", 30, "40", 50]
    comparison_results = compare_adjacent(sample_data)
    for index, val1, val2, status in comparison_results:
        print(f"Index {index}: Comparing {val1} and {val2}. Result: {status}")