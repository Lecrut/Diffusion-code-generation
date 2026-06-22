import math

def calculate_mean(results):
    if not results:
        raise ValueError("List of test results must not be empty")
    total = math.fsum(results)
    mean = total / len(results)
    return mean

if __name__ == '__main__':
    sample_results = [85.5, 90.2, 78.3, 92.1, 88.9, 95.0, 82.4, 91.6, 87.7, 93.3]
    mean_result = calculate_mean(sample_results)
    print(mean_result)