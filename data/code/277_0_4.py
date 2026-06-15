def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample_numbers = [15, 27, 8, 42, 11]
    result = calculate_sum(sample_numbers)
    print(result)