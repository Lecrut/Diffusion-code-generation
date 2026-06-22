import statistics

def compute_mean(test_results):
    return statistics.mean(test_results)

if __name__ == '__main__':
    sample_data = [85.5, 90.0, 78.25, 92.5, 88.75]
    result = compute_mean(sample_data)
    print(result)