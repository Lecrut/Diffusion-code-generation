def find_adjacent_greater_indices(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_values = [10, 20, 30, 25, 40, 50]
    result = find_adjacent_greater_indices(sample_values)
    print(result)