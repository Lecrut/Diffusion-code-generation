import statistics

def compute_mean(test_results):
    return statistics.mean(test_results)

if __name__ == '__main__':
    sample_results = [85.5, 90.2, 78.9, 92.1, 88.7, 95.3, 81.4, 89.6, 93.8, 76.2]
    result = compute_mean(sample_results)
    print(result)