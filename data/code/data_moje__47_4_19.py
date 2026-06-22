import math

def calculate_mean(test_results):
    if not test_results:
        return 0.0
    total_sum = math.fsum(test_results)
    return total_sum / len(test_results)

if __name__ == '__main__':
    sample_results = [10.1, 10.2, 10.3, 10.4, 10.5]
    print(calculate_mean(sample_results))