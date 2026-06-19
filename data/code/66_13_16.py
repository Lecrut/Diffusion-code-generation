def find_strictly_increasing_pairs(numbers):
    def validate_input(numbers):
        if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
            raise ValueError("Input must be a list of integers.")
        if len(numbers) < 2:
            return []

    validated_numbers = validate_input(numbers)
    increasing_pairs_indices = []
    
    for i in range(len(validated_numbers) - 1):
        if validated_numbers[i] < validated_numbers[i + 1]:
            increasing_pairs_indices.append((i, i + 1))
    
    return increasing_pairs_indices

if __name__ == '__main__':
    sample_input = [1, 3, 2, 5, 7, 6, 8]
    result = find_strictly_increasing_pairs(sample_input)
    print(result)