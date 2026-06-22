import statistics

def calculate_median(values):
    return statistics.median(values)

if __name__ == '__main__':
    sample_values = [5, 3, 1, 4, 2]
    median_result = calculate_median(sample_values)
    print(median_result)