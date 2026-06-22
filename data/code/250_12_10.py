def calculate_average(numbers):
    TOTAL = 0
    COUNT = 0

    for num in numbers:
        if isinstance(num, int):
            TOTAL += num
            COUNT += 1
        else:
            print(f"Error: '{num}' is not a valid integer. Skipping.")

    if COUNT > 0:
        average = TOTAL / COUNT
        return average
    else:
        return None

if __name__ == '__main__':
    sample_numbers = [10, 20, 'a', 30, 40]
    result = calculate_average(sample_numbers)
    print(f"The average of the entered numbers is: {result}")