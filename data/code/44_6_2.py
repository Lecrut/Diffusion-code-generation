def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    empty_data = []
    result = calculate_mean(sample_data)
    empty_result = calculate_mean(empty_data)
    print(result)
    print(empty_result)