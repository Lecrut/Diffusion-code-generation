def compare_adjacent(numbers):
    result = []
    length = len(numbers)
    for i in range(length - 1):
        is_ascending = numbers[i] < numbers[i + 1]
        result.append(is_ascending)
    return result

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    comparison_results = compare_adjacent(sample_values)
    print(comparison_results)