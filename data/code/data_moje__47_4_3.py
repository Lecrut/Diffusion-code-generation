import math

def calculate_mean(results):
    if not results:
        raise ValueError("Cannot calculate mean of empty list")
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_results = [85.5, 90.2, 78.9, 92.1, 88.4]
    mean_result = calculate_mean(sample_results)
    print(mean_result)