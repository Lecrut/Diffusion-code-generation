def compare_adjacent_pairs(numbers):
    return [max(a, b) for a, b in zip(numbers, numbers[1:])]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = compare_adjacent_pairs(sample_values)
    print(result)