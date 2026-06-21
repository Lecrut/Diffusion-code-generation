import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    result_mean, result_median, result_std_dev = calculate_stats(sample_data)
    print(f"Mean: {result_mean}")
    print(f"Median: {result_median}")
    print(f"Standard Deviation: {result_std_dev}")