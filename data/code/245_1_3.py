import math
def check_equal_area(radius, length):
    circle_area = math.pi * (radius ** 2)
    rectangle_area = length * length
    return circle_area == rectangle_area
if __name__ == '__main__':
    r1 = 5.0
    l1 = 25.0
    print(f"Radius: {r1}, Length: {l1}, Equal Area: {check_equal_area(r1, l1)}")
    r2 = 1.0
    l2 = math.pi
    print(f"Radius: {r2}, Length: {l2}, Equal Area: {check_equal_area(r2, l2)}")
    r3 = 3.0
    l3 = 9.0
    print(f"Radius: {r3}, Length: {l3}, Equal Area: {check_equal_area(r3, l3)}")