def check_ascending_pairs(numbers):
    n = len(numbers)
    results = []
    for i in range(n - 1):
        if numbers[i] < numbers[i+1]:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_list = [1, 3, 2, 4, 5]
    comparison_results = check_ascending_pairs(sample_list)
    print(comparison_results)