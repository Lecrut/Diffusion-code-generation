import statistics

def compare_data_sets(data_set_1, data_set_2):
    if not all(isinstance(x, (int, float)) for x in data_set_1) or not all(isinstance(x, (int, float)) for x in data_set_2):
        raise ValueError("Both data sets must contain only numeric values.")
    
    stats_1 = {
        'mean': statistics.mean(data_set_1),
        'median': statistics.median(data_set_1),
        'std_dev': statistics.stdev(data_set_1)
    }
    
    stats_2 = {
        'mean': statistics.mean(data_set_2),
        'median': statistics.median(data_set_2),
        'std_dev': statistics.stdev(data_set_2)
    }
    
    return {
        'data_set_1': stats_1,
        'data_set_2': stats_2
    }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [3, 4, 5, 6, 7]
    
    result = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(result)