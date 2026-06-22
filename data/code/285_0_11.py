def compare_adjacent(data):
    comparison_map = {True: 'increasing', False: 'decreasing'}
    results = []
    for i in range(len(data) - 1):
        a, b = data[i], data[i+1]
        if a > b:
            results.append(comparison_map[a > b])
        elif a < b:
            results.append(comparison_map[a < b])
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = compare_adjacent(sample_data)
    print(comparison_results)