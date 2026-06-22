def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [5, 12, 18, 25]
    result = calculate_mean(sample_values)
    print(result)