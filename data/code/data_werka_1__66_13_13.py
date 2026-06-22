def find_adjacent_increasing_pairs(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 7, 2, 9]
    result = find_adjacent_increasing_pairs(sample_values)
    print(result)