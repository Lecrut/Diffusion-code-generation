def find_adjacent_greater_indices(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_values = [3, 8, 6, 7, 5, 9, 2, 4]
    result = find_adjacent_greater_indices(sample_values)
    print(result)