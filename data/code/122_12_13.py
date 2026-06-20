def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count else 0

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    average = calculate_average(sample_values)
    print(average)