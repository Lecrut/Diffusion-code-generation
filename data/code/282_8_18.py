def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_numbers = [15, -3, 20, -7, 4]
    result = calculate_total(sample_numbers)
    print(result)