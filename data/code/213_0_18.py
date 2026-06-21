import statistics

def calculate_stats(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    
    return mean, median, std_dev

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    mean, median, std_dev = calculate_stats(sample_values)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")