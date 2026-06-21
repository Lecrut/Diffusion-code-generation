def calculate_mean(numbers):
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    mean_value = total_sum / count
    return mean_value

if __name__ == '__main__':
    sample_values = [20, 40, 60, 80, 100]
    print(calculate_mean(sample_values))
    empty_list = []
    print(calculate_mean(empty_list))