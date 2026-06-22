import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    test_results = [85, 90, 78, 92, 88, 76, 95, 82, 89, 93]
    result = compute_mean(test_results)
    print(result)