import statistics

def calculate_statistics(data_set):
    if not data_set:
        raise ValueError("Data set cannot be empty")
    
    mean_value = statistics.mean(data_set)
    median_value = statistics.median(data_set)
    std_dev_value = statistics.stdev(data_set)
    
    return {
        'mean': mean_value,
        'median': median_value,
        'std_dev': std_dev_value
    }

def compare_data_sets(data_set_1, data_set_2):
    if not all([data_set_1, data_set_2]):
        raise ValueError("Both data sets must be provided")
    
    stats_1 = calculate_statistics(data_set_1)
    stats_2 = calculate_statistics(data_set_2)
    
    return {
        'set_1': stats_1,
        'set_2': stats_2
    }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [6, 7, 8, 9, 10]
    
    result = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(result)