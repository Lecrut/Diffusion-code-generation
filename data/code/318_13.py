def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        try:
            if a == b:
                results.append((i, "Equal"))
            else:
                results.append((i, "Not Equal", a, b))
        except TypeError as e:
            print(f"Error comparing elements at index {i}: {e}")
            results.append((i, "Type Error", type(a).__name__, type(b).__name__))
    return results
if __name__ == '__main__':
    sample_data = [10, 20, "30", 40, "error"]
    comparison_results = compare_adjacent(sample_data)
    for index, status, *details in comparison_results:
        print(f"Index {index}: Status: {status}")
        if status == "Not Equal":
            print(f"  Values: {details[0]} vs {details[1]}")
        elif status == "Type Error":
            print(f"  Types involved: {details[0]} vs {details[1]}")
    print("\nRaw Results:")
    print(comparison_results)