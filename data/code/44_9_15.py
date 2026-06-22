def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(sample_numbers)
    print(average)