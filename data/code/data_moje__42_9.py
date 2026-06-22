import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    print(ellipse_area(sample_a, sample_b))