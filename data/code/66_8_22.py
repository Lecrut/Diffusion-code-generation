def compare_adjacent(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    sample_values = [7, 3, 5, 2, 8, 6]
    comparison_results = compare_adjacent(sample_values)
    print(comparison_results)