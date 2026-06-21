def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    avg = calculate_average(sample_numbers)
    print(avg)