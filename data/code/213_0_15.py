import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    results = calculate_stats(sample_values)
    print(f"Mean: {results[0]}")
    print(f"Median: {results[1]}")
    print(f"Standard Deviation: {results[2]}")