def sum_large_sequence(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [123456789.12345, 987654321.12345, 111111111.12345]
    result = sum_large_sequence(sample_numbers)
    print(result)