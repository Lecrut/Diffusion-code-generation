import statistics

MEAN_THRESHOLD = 0.5

def calculate_mean(values):
    return statistics.mean(values) if len(values) >= MEAN_THRESHOLD else 0

if __name__ == '__main__':
    sample_values = [10, 20, 30]
    average = calculate_mean(sample_values)
    print(average)