def sum_sequence(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    result = sum_sequence(sample_values)
    print(result)