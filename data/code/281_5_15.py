def sum_eight_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = (12, 24, 36, 48, 60, 72, 84, 96)
    result = sum_eight_numbers(sample_values)
    print(result)