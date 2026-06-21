def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    avg_result = calculate_average(sample_values)
    print(avg_result)