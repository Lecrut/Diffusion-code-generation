import statistics

MEAN = 'mean'
MEDIAN = 'median'
STDDEV = 'stddev'

def calculate_statistics(data):
    try:
        mean_value = statistics.mean(data)
        median_value = statistics.median(data)
        stddev_value = statistics.stdev(data)
        return {MEAN: mean_value, MEDIAN: median_value, STDDEV: stddev_value}
    except (statistics.StatisticsError, TypeError) as e:
        return f"Error calculating statistics: {e}"

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    stats = calculate_statistics(sample_list)
    print(f"List: {sample_list}")
    for stat_type, value in stats.items():
        print(f"{stat_type.capitalize()}: {value:.2f}")