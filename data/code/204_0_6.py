import statistics

def find_middle_value(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [10, 23, 5, 8, 3]
    print(find_middle_value(sample_values))