def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [10, -5, 3, -2, 4]
    print(calculate_total(sample_numbers))