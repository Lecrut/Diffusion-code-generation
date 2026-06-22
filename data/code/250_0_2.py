import statistics

def compute_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0, 6.7]
    print(compute_mean(sample_values))