def find_adjacent_greater_indices(numbers):
    return [i for i in range(len(numbers) - 1) if numbers[i + 1] > numbers[i]]

if __name__ == '__main__':
    sample_numbers = [1, 4, 3, 7, 6, 9]
    result = find_adjacent_greater_indices(sample_numbers)
    print(result)