import statistics

def compute_mean(test_results):
    if not test_results:
        return 0.0
    return statistics.mean(test_results)

if __name__ == '__main__':
    sample_data = [85.5, 90.0, 78.5, 92.0, 88.5]
    result = compute_mean(sample_data)
    print(result)