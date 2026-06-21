def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [7],
        []
    ]
    
    for idx, sample in enumerate(sample_values):
        try:
            print(f"Largest in sample {idx + 1}: {find_largest(sample)}")
        except ValueError as e:
            print(e)