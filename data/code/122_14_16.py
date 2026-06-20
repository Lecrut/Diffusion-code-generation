def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    avg = calculate_average(sample_numbers)
    print(avg)