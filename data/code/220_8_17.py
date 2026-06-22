def calculate_average(numbers):
    if not hasattr(numbers, '__iter__'):
        raise ValueError("Input must be iterable")
    total = sum(numbers)
    count = len(numbers)
    return float(total) / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(calculate_average(sample_list))