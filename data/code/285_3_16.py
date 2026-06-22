def compare_adjacent_pairs(numbers):
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 6]
    result = compare_adjacent_pairs(sample_numbers)
    print(result)