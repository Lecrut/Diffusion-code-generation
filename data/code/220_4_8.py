def calculate_average(numbers):
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average_result = calculate_average(sample_numbers)
    print(average_result)