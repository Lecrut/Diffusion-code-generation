def sum_sequence(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_values)
    print(result)