def find_adjacent_greater_pairs(numbers):
    indices = []
    try:
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                indices.append((i, i + 1))
    except TypeError:
        raise ValueError("Input must be a list of integers.")
    return indices

if __name__ == '__main__':
    sample_list = [5, 3, 8, 6, 7, 9]
    result = find_adjacent_greater_pairs(sample_list)
    print(result)