import math

def calculate_mean(results):
    if not results:
        raise ValueError("The input list must not be empty")
    total = math.fsum(results)
    mean = total / len(results)
    return mean

if __name__ == '__main__':
    test_results = [23.5, 25.1, 24.9, 26.3, 24.2]
    result = calculate_mean(test_results)
    print(result)