def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = calculate_average(sample_numbers)
    print(result)