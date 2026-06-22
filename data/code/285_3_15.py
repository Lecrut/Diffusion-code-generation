def compare_adjacent_pairs(numbers):
    results = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 6, 9]
    comparison_results = compare_adjacent_pairs(sample_list)
    print(comparison_results)