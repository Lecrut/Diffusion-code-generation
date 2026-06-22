import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    sample_a = 5.0
    sample_b = 3.0
    result = ellipse_area(sample_a, sample_b)
    print(result)