def compare_adjacent(numbers):
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [1, 3, 2, 4, 5]
    result = compare_adjacent(sample_values)
    print(result)