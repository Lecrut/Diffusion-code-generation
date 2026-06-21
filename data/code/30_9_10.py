import math
PI_VALUE = math.pi
def compute_circle_area(radius):
    return PI_VALUE * radius * radius
if __name__ == '__main__':
    TEST_RADIUS = 12
    computed_area = compute_circle_area(TEST_RADIUS)
    print(computed_area)