def calculate_average(numbers):
    total_sum = 0
    count = len(numbers)
    for number in numbers:
        total_sum += number
    return total_sum / count if count > 0 else 0.0

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(sample_numbers)
    print(average)