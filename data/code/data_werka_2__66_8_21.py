def compare_adjacent(numbers):
    comparisons = []
    for i in range(len(numbers) - 1):
        first_number = numbers[i]
        second_number = numbers[i + 1]
        is_ascending = first_number < second_number
        comparisons.append(is_ascending)
    return comparisons

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 45]
    result = compare_adjacent(sample_values)
    print(result)