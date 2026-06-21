def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    average = calculate_average(sample_numbers)
    print(average)