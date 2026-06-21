import statistics

MEAN = 'mean'
MEDIAN = 'median'
STDEV = 'std_dev'

def calculate_statistics(data):
    return {
        MEAN: statistics.mean(data),
        MEDIAN: statistics.median(data),
        STDEV: statistics.stdev(data)
    }

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    stats = calculate_statistics(sample_list)
    print(f"List: {sample_list}")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")