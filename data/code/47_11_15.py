import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [85, 90, 78, 92, 88, 95, 82, 89, 91, 87]
    result = compute_mean(test_results)
    print(result)