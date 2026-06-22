def calculate_average(numbers):
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    average = calculate_average(sample_data)
    print(average)