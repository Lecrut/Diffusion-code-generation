import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [85.5, 90.0, 78.5, 92.0, 88.0, 95.0, 82.0]
    mean_value = compute_mean(test_results)
    print(mean_value)