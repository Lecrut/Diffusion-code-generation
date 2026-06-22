import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    test_results = [85.5, 90.0, 78.5, 92.0, 88.0]
    result = compute_mean(test_results)
    print(result)