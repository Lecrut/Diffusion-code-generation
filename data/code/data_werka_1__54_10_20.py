import math
PI = math.pi

def compute_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    test_radius = 10.0
    print(compute_circle_area(test_radius))