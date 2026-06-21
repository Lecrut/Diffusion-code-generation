def calculate_mean(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    mean = total_sum / count
    return mean

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    result = calculate_mean(sample_values)
    print(result)