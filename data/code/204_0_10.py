import statistics

def find_middle_value(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)