def find_strictly_increasing_pairs(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_numbers = [5, 3, 8, 6, 7, 9]
    result = find_strictly_increasing_pairs(sample_numbers)
    print(result)