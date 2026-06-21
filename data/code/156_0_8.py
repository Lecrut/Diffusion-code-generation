def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    avg_result = calculate_average(sample_values)
    print(avg_result)