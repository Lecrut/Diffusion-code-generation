def find_strictly_increasing_pairs(numbers):
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_list = [5, 3, 8, 6, 9, 10, 2]
    result_indices = find_strictly_increasing_pairs(sample_list)
    print(result_indices)