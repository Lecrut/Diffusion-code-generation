def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    avg = calculate_average(sample_numbers)
    print(avg)