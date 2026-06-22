def calculate_mean(numbers):
    if not numbers:
        return 0
    total_sum = 0
    count = 0
    for number in numbers:
        total_sum += number
        count += 1
    return total_sum / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)