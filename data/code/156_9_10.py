def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    avg_result = calculate_average(sample_data)
    print(f"The average of {sample_data} is: {avg_result}")