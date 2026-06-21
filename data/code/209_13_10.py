def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample_values = [18, 27, 36, 45, 54]
    result = calculate_average(sample_values)
    print(result)