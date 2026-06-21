def calculate_mean(data):
    if not data:
        return 0
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    return average

def calculate_median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

def calculate_std_deviation(data):
    if not data:
        return None
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return std_dev

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    avg = calculate_mean(sample_list)
    median = calculate_median(sample_list)
    std_dev = calculate_std_deviation(sample_list)
    
    print(f"List: {sample_list}")
    print(f"Average: {avg}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")