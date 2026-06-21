def calculate_mean(data):
    return sum(data) / len(data) if data else 0

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_std_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78, 90]
    mean_val = calculate_mean(sample_list)
    median_val = calculate_median(sample_list)
    std_dev_val = calculate_std_deviation(sample_list)
    
    print(f"List: {sample_list}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Standard Deviation: {std_dev_val}")