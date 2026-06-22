import statistics

def compute_mean(test_results):
    return statistics.mean(test_results)

if __name__ == '__main__':
    sample_results = [85.5, 92.0, 78.3, 95.1, 88.7, 91.2, 87.9, 93.4, 89.6, 90.1]
    result = compute_mean(sample_results)
    print(result)