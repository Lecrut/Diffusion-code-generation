def calculate_average(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_numbers = [3, 6, 9, 12, 15]
    avg_result = calculate_average(sample_numbers)
    print(f"The average of {sample_numbers} is: {avg_result}")