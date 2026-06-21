import statistics

def find_middle_value(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [12, 345, 67890, 234, 567]
    print(find_middle_value(sample_values))