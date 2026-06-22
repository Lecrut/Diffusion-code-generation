import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_results = [10.5, 20.3, 30.1, 40.8, 50.4]
    mean_result = calculate_mean(sample_results)
    print(mean_result)