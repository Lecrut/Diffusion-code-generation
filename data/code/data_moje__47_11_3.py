import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [23, 45, 67, 89, 12, 54, 34, 76, 90, 11]
    result = compute_mean(test_results)
    print(result)