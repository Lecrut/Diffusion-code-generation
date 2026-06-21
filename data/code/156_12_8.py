def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(sample_numbers)
    print(avg)