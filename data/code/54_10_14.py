import math

def compute_area(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    test_radius = 10.0
    result = compute_area(test_radius)
    print(result)