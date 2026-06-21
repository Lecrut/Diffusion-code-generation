import statistics

def compute_median(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    print(compute_median(sample_values))