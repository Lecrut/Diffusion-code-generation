import statistics

def compute_stats(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean, median, std_dev = compute_stats(sample_data)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")