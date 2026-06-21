import statistics

def find_middle_value(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    median_value = find_middle_value(sample_values)
    print(median_value)