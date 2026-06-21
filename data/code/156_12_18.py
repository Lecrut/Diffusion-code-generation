def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    length = len(numbers)
    average = total / length
    return average

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_average(sample_numbers))