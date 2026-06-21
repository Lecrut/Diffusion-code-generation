def calculate_average(numbers):
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(calculate_average(sample_values))