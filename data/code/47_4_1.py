import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    test_data = [10.0, 20.0, 30.0, 40.0, 50.0]
    print(calculate_mean(test_data))