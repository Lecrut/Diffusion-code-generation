def calculate_mean(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    mean_value = total_sum / count
    return mean_value

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8, 10]
    result = calculate_mean(sample_numbers)
    print(result)