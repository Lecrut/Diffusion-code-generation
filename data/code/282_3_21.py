def sum_large_sequence(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [123.456, 789.123, 432.109, 987.654]
    result = sum_large_sequence(sample_values)
    print(result)