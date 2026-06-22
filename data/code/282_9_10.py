def validate_sequence(sequence: list[int]) -> bool:
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    for item in sequence:
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")
    return True

def sum_sequence(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    if validate_sequence(sample_numbers):
        result = sum_sequence(sample_numbers)
        print(result)