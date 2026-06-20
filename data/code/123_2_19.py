import math

def calculate_floating_point_sum(iterable):
    return math.fsum(iterable)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    total = calculate_floating_point_sum(sample_values)
    print(total)