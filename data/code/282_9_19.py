def validate_sequence(sequence: list[int]) -> None:
    if not isinstance(sequence, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in sequence):
        raise ValueError("All elements in the list must be integers.")

def calculate_sum(sequence: list[int]) -> int:
    validate_sequence(sequence)
    total = 0
    for number in sequence:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(sample_numbers)
    print(result)