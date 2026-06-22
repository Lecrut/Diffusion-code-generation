import math

def compute_average(data: list) -> float:
    total_sum = math.fsum(data)
    count = len(data)
    average = total_sum / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    result = compute_average(sample_values)
    print(result)