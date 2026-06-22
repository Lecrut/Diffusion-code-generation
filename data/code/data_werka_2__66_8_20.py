def compare_adjacent(numbers):
    COMPARISON_THRESHOLD = 0
    result = []
    for i in range(len(numbers) - 1):
        is_ascending = numbers[i] < numbers[i + 1]
        result.append(is_ascending)
    return result

if __name__ == '__main__':
    sample_values = [7, 3, 5, 2, 8, 6, 7]
    comparison_results = compare_adjacent(sample_values)
    print(comparison_results)