def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))