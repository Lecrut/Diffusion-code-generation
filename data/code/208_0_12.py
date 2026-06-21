import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [2.5, 3.0, 4.5, 6.0, 7.5]
    result = compute_mean(sample_values)
    print(result)