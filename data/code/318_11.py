def compare_adjacent(numbers):
    results = []
    for i in range(len(numbers) - 1):
        a = numbers[i]
        b = numbers[i+1]
        results.append((a, b))
    return results
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    comparison_results = compare_adjacent(sample_list)
    print(comparison_results)