def calculate_mean(numbers):
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    mean_value = total_sum / count
    return mean_value

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25]
    result = calculate_mean(sample_values)
    print(result)

    empty_list = []
    result = calculate_mean(empty_list)
    print(result)