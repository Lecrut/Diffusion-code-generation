import math

def calculate_mean(test_results):
    if not test_results:
        return 0.0
    total = math.fsum(test_results)
    return total / len(test_results)

if __name__ == '__main__':
    sample_data = [85.5, 90.2, 78.9, 92.3, 88.1]
    result = calculate_mean(sample_data)
    print(result)