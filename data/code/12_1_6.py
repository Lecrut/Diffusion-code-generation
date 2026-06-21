import statistics

def find_median(data):
    return statistics.median(data)

if __name__ == '__main__':
    sample_data = [10, 2, 4, 7, 9, 3, 8]
    result = find_median(sample_data)
    print(result)