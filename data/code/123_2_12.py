import math

def sum_floating_point_values(values):
    return math.fsum(values)

if __name__ == '__main__':
    sample_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    result = sum_floating_point_values(sample_data)
    print(result)