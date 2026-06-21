def precise_sum(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1.23456789, 2.34567890, 3.45678901, -4.56789012]
    result = precise_sum(sample_numbers)
    print(result)