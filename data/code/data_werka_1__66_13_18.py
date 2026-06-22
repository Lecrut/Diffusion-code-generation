def find_strictly_increasing_pairs(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input must be a list of integers.")
    
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_input = [1, 3, 2, 5, 7, 6, 8]
    try:
        result = find_strictly_increasing_pairs(sample_input)
        print(result)
    except ValueError as e:
        print(e)