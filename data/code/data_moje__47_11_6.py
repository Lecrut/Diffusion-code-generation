import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [85.5, 92.0, 78.5, 95.0, 88.5, 91.0, 84.0, 90.5]
    result = compute_mean(test_results)
    print(result)