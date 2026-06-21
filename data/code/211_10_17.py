import statistics

def calculate_statistics(data_set):
    if not data_set:
        raise ValueError("Data set cannot be empty")
    
    mean = statistics.mean(data_set)
    median = statistics.median(data_set)
    std_dev = statistics.stdev(data_set)
    
    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev
    }

def compare_data_sets(data_set_1, data_set_2):
    stats_1 = calculate_statistics(data_set_1)
    stats_2 = calculate_statistics(data_set_2)
    
    comparison_result = {
        'stats_1': stats_1,
        'stats_2': stats_2
    }
    
    return comparison_result

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [6, 7, 8, 9, 10]
    
    result = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(result)