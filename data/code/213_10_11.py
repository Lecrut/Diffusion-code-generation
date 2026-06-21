import statistics

def calculate_statistics(numbers):
    if not numbers:
        return None, None, None
    average = statistics.mean(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers)
    return average, median, std_dev

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    avg, med, stdev = calculate_statistics(sample_list)
    print(f"List: {sample_list}")
    print(f"Average: {avg}")
    print(f"Median: {med}")
    print(f"Standard Deviation: {stdev}")