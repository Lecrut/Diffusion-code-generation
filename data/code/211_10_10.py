import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)
    return {'mean': mean, 'median': median, 'std_dev': std_dev}

def compare_data_sets(data_set_1, data_set_2):
    stats_1 = calculate_statistics(data_set_1)
    stats_2 = calculate_statistics(data_set_2)
    return {
        'set_1': stats_1,
        'set_2': stats_2
    }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [3, 4, 5, 6, 7]
    result = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(result)