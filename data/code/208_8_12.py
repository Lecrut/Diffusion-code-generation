def compute_average(values):
    valid_numbers = [value for value in values if isinstance(value, int) and value > 0]
    if not valid_numbers:
        return None
    total_sum = sum(valid_numbers)
    count = len(valid_numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data = [15, 25, "a", 35, 45.0]
    result = compute_average(sample_data)
    print(result)