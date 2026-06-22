MAX_COMPARISON = max

def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if a < b:
            results.append(b)
        elif a > b:
            results.append(a)
        else:
            results.append(a)
    return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3, 0]
    comparison_results = compare_adjacent(sample_data)
    print(comparison_results)