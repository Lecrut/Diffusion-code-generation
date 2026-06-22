def sum_large_sequence(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [123456789.123, 987654321.987, 111111111.111, 222222222.222, 333333333.333]
    result = sum_large_sequence(sample_values)
    print(result)