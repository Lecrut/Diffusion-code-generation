def calculate_mean(numbers):
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    mean_value = total_sum / count
    return mean_value

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    print(calculate_mean(sample_values))
    empty_list = []
    print(calculate_mean(empty_list))