def calculate_average(numbers):
    if not isinstance(numbers, list):
        return None
    if not numbers:
        return 0
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        return None

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    average_result = calculate_average(sample_numbers)
    print(f"The average of {sample_numbers} is {average_result}")