def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [25, 35, 45, 55, 65]
    result = calculate_average(sample_numbers)
    print(f"The average of {sample_numbers} is: {result}")