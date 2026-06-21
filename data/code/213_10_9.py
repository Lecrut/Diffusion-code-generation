import statistics

def compute_statistics(data):
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count if count > 0 else 0
    median_value = statistics.median(data) if count > 0 else None
    std_deviation = statistics.stdev(data, xbar=average) if count > 1 else 0
    return total_sum, average, median_value, std_deviation

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    total, avg, median, std_dev = compute_statistics(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")