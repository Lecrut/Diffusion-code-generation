import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_values = [35, 42, 57, 61, 70]
    mean, median, std_dev = calculate_stats(sample_values)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")