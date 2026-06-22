import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_results = [95.5, 88.2, 76.4, 92.1, 85.7]
    mean_value = calculate_mean(sample_results)
    print(mean_value)