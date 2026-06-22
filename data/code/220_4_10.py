def calculate_average(numbers):
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    average = total_sum / count
    return round(average, 10)

if __name__ == '__main__':
    sample_numbers = [10.5, 20.3, 30.7, 40.2]
    print(calculate_average(sample_numbers))