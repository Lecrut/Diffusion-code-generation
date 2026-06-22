def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(num for num in numbers if isinstance(num, (int, float)))
    count = len(numbers)
    valid_count = count - (count - len([num for num in numbers if isinstance(num, (int, float))]))

    if valid_count == 0:
        return 0

    average = total / valid_count
    return average

if __name__ == '__main__':
    sample_numbers = [10, '20', 30, 40.5, None]
    result = calculate_average(sample_numbers)
    print(f"The average of the entered numbers is: {result}")