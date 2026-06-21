def calculate_average(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data1 = [25, 35, 45, 55, 65]
    avg1 = calculate_average(sample_data1)
    print(f"The average of {sample_data1} is: {avg1}")

    sample_data2 = [100, 200, 300, 400]
    avg2 = calculate_average(sample_data2)
    print(f"The average of {sample_data2} is: {avg2}")