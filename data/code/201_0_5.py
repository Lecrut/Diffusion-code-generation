def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_average(sample_values)
    print(result)