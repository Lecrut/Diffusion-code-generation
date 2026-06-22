import math

def calculate_mean(results):
    if not results:
        return 0.0
    return math.fsum(results) / len(results)

if __name__ == '__main__':
    test_results = [1.1, 2.2, 3.3, 4.4, 5.5]
    mean_value = calculate_mean(test_results)
    print(mean_value)