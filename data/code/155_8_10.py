def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(sum_numbers(sample_numbers))