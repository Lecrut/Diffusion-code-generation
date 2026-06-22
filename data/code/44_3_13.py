def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = calculate_average(sample_numbers)
    print(result)