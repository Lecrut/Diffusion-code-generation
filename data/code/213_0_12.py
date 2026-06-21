import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    stats = calculate_stats(sample_data)
    print(f"Mean: {stats[0]}")
    print(f"Median: {stats[1]}")
    print(f"Standard Deviation: {stats[2]}")