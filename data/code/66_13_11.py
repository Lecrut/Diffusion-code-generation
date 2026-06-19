def find_adjacent_greater_indices(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 6, 7, 4]
    result = find_adjacent_greater_indices(sample_numbers)
    print(result)