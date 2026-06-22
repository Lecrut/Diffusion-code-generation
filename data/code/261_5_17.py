import statistics

def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return statistics.median(data)

if __name__ == '__main__':
    sample1 = [1.0, 2.5, 3.0, 4.5, 5.0]
    sample2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
    sample3 = [1.0, 2.0, 3.0, 4.0]
    sample4 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

    print(calculate_median(sample1))
    print(calculate_median(sample2))
    print(calculate_median(sample3))
    print(calculate_median(sample4))