import statistics

def compute_statistics(data_set):
    return {
        'mean': statistics.mean(data_set),
        'median': statistics.median(data_set),
        'std_dev': statistics.stdev(data_set)
    }

def compare_data_sets(data_set_1, data_set_2):
    stats_1 = compute_statistics(data_set_1)
    stats_2 = compute_statistics(data_set_2)
    
    return {
        'data_set_1': stats_1,
        'data_set_2': stats_2
    }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [3, 4, 5, 6, 7, 8, 9, 10]
    
    result = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(result)