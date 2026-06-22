def sum_sequence(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("All elements must be integers")
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(sum_sequence(sample_numbers))