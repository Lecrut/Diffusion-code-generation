def calculate_average(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    avg_result = calculate_average(sample_data)
    print(avg_result)