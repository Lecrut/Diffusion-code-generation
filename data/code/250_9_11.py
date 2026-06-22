import math

def compute_average(data: list) -> float:
    total_sum = math.fsum(data)
    count = len(data)
    if count == 0:
        return 0.0
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    result = compute_average(sample_values)
    print(result)