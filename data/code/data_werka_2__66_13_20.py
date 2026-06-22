def find_adjacent_greater_indices(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_list = [10, 9, 8, 7, 6, 5, 4]
    result = find_adjacent_greater_indices(sample_list)
    print(result)