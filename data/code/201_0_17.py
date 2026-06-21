def calculate_average(numbers):
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    mean = total_sum / count
    return mean

if __name__ == '__main__':
    sample_values = [3, 6, 9, 12, 15]
    result = calculate_average(sample_values)
    print(result)