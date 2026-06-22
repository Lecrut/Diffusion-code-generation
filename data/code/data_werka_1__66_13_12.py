def find_strictly_increasing_pairs(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers.")
    
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 7, 9, 2]
    result = find_strictly_increasing_pairs(sample_values)
    print(result)