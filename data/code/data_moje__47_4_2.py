import math

def calculate_mean(test_results):
    if not test_results:
        return 0.0
    total = math.fsum(test_results)
    return total / len(test_results)

if __name__ == '__main__':
    sample_results = [99.99, 100.01, 100.0, 98.5, 100.0]
    result = calculate_mean(sample_results)
    print(result)