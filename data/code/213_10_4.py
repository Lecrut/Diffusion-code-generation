import statistics

def compute_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    mean, median, std_dev = compute_stats(sample_values)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")