def sum_large_sequence(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [100.5, 200.3, 300.7, 400.2, 500.8]
    result = sum_large_sequence(sample_values)
    print(result)