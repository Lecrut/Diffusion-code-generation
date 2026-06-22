import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    sample_data = [10.5, 20.1, 30.4, 40.2, 50.3]
    print(calculate_mean(sample_data))