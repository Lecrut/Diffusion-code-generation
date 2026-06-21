import statistics

def find_middle_value(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [7, 3, 9, 1, 5]
    print(find_middle_value(sample_values))