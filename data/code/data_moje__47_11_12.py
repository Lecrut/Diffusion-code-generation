import statistics

def compute_mean(results):
    return statistics.mean(results)

if __name__ == '__main__':
    test_results = [85.5, 90.0, 78.25, 92.5, 88.75]
    mean_value = compute_mean(test_results)
    print(mean_value)