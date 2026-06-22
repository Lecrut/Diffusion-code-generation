def calculate_mean(numbers):
    if not numbers:
        return None
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [10.0, 20.0, 30.0, 40.0, 50.0]
    result = calculate_mean(sample_values)
    print(result)
    empty_result = calculate_mean([])
    print(empty_result)