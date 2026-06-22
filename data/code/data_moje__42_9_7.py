import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a_val = 5.0
    b_val = 3.0
    result = ellipse_area(a_val, b_val)
    print(result)