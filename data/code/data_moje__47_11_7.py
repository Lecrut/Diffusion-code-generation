import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    test_results = [10.5, 20.3, 15.1, 18.9, 22.4, 19.8]
    result = compute_mean(test_results)
    print(result)