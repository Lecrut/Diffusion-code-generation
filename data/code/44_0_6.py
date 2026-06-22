def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = 0
    count = len(numbers)
    for num in numbers:
        total += num
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = calculate_average(sample_numbers)
    print(result)