import statistics

def calculate_median(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    median_value = calculate_median(sample_values)
    print(median_value)