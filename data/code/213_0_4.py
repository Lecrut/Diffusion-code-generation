import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_data = [5, 12, 7, 3, 18, 9]
    stats = calculate_stats(sample_data)
    print(f"Mean: {stats[0]}")
    print(f"Median: {stats[1]}")
    print(f"Standard Deviation: {stats[2]}")