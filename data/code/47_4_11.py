import math

def calculate_mean(results):
    if not results:
        return 0.0
    return math.fsum(results) / len(results)

if __name__ == '__main__':
    test_results = [10.1, 20.2, 30.3, 40.4, 50.5]
    result = calculate_mean(test_results)
    print(result)