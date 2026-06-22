def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_average(sample_data)
    print(result)