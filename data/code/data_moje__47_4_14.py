import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_results = [85.5, 90.2, 78.9, 92.1, 88.4, 76.3, 95.0, 82.7]
    result = calculate_mean(sample_results)
    print(result)