def sum_large_sequence(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(sum_large_sequence(sample_numbers))