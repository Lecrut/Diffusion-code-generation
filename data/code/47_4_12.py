import math

def calculate_mean(results):
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_results = [10.5, 20.3, 30.1, 40.7, 50.2]
    mean_value = calculate_mean(sample_results)
    print(mean_value)