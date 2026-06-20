import math

def sum_floats(iterable):
    return math.fsum(iterable)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    result = sum_floats(sample_values)
    print(result)