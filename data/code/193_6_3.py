def sum_mixed_numbers(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, int):
            total += number
        elif isinstance(number, float):
            total += number
    return total

if __name__ == '__main__':
    sample_values = [10, 2.5, -3, 4.75]
    result = sum_mixed_numbers(sample_values)
    print(result)