import math

def compute_circle_area(radius):
    return float(math.pi * radius * radius)

if __name__ == '__main__':
    print(compute_circle_area(5))
    print(compute_circle_area(10))
    print(compute_circle_area(1))