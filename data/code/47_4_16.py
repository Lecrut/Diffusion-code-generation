import math

def calculate_mean(test_results):
    if not test_results:
        return 0.0
    return math.fsum(test_results) / len(test_results)

if __name__ == '__main__':
    sample_data = [10.1, 20.2, 30.3, 40.4, 50.5]
    result = calculate_mean(sample_data)
    print(result)