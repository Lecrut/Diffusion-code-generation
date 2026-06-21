def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    result = calculate_average(sample_values)
    print(result)