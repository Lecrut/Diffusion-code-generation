import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [85.5, 90.0, 78.2, 92.1, 88.7]
    result = compute_mean(test_results)
    print(result)