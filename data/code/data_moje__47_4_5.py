import math

def calculate_mean(results):
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    test_results = [0.1, 0.2, 0.3, 0.4, 0.5]
    mean_value = calculate_mean(test_results)
    print(mean_value)