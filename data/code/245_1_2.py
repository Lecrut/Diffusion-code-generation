import math
def check_equal_area(radius, length):
    circle_area = math.pi * (radius ** 2)
    rectangle_area = length * length
    return circle_area == rectangle_area
if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.0
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {check_equal_area(r1, l1)}")
    r2 = 3.0
    l2 = math.pi * 3.0                                                     
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {check_equal_area(r2, l2)}")
    r3 = 1.0
    l3 = math.pi                                                     
    print(f"Radius: {r3}, Length: {l3}, Areas Equal: {check_equal_area(r3, l3)}")
    r4 = 2.0
    l4 = 4.0                                                      
    print(f"Radius: {r4}, Length: {l4}, Areas Equal: {check_equal_area(r4, l4)}")