def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_values)
    print(result)
    empty_result = calculate_mean([])
    print(empty_result)
    single_result = calculate_mean([42])
    print(single_result)
    negative_result = calculate_mean([-1, -2, -3])
    print(negative_result)
    mixed_result = calculate_mean([1.5, 2.5, 3.0])
    print(mixed_result)