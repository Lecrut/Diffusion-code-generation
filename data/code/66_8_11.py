def compare_adjacent(numbers):
    results = []
    for i in range(len(numbers) - 1):
        results.append(numbers[i] < numbers[i + 1])
    return results

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = compare_adjacent(sample_array)
    print(result)