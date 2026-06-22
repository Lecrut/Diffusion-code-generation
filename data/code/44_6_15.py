def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_values)
    print(result)
    empty_list = []
    empty_result = calculate_mean(empty_list)
    print(empty_result)