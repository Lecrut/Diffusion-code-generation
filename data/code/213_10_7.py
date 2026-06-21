import statistics

def compute_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return mean, median, std_dev

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    mean, median, std_dev = compute_statistics(sample_numbers)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")