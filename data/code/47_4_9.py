import math

def calculate_mean(test_results):
    if not test_results:
        return 0.0
    total_sum = math.fsum(test_results)
    count = len(test_results)
    return total_sum / count

if __name__ == '__main__':
    sample_results = [95.5, 87.2, 91.8, 76.4, 88.9]
    mean_value = calculate_mean(sample_results)
    print(mean_value)