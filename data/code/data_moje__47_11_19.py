import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [10, 20, 30, 40, 50]
    result = compute_mean(test_results)
    print(result)