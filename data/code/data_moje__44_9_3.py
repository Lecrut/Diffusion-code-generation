def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    predefined_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(predefined_numbers)
    print(average)