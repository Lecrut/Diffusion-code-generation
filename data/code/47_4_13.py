import math

def calculate_mean(results):
    if not results:
        raise ValueError("Cannot calculate mean of an empty list")
    return math.fsum(results) / len(results)

if __name__ == '__main__':
    sample_results = [95.5, 87.3, 92.1, 88.9, 91.2]
    print(calculate_mean(sample_results))