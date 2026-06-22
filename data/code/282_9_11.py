def sum_sequence(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = sum_sequence(sample_values)
    print(result)