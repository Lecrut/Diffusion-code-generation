import statistics

def find_median(data):
    if not data:
        raise ValueError("Data list must not be empty")
    return statistics.median(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_median(sample_data)
    print(result)