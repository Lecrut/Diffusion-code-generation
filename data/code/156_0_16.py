def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25]
    result = calculate_average(sample_values)
    print(result)