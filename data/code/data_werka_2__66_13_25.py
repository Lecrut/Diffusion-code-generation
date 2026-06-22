def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements in the list must be integers.")

def find_adjacent_greater_indices(numbers):
    validate_input(numbers)
    indices = []
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_numbers = [4, 1, 7, 3, 8, 5, 9]
    result = find_adjacent_greater_indices(sample_numbers)
    print(result)