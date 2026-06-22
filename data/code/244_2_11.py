import math
A_SEMI_MAJOR = 3
B_SEMI_MINOR = 2
C_SEMI_MAJOR = 4
D_SEMI_MINOR = 1

def area_of_ellipse(a, b):
    return math.pi * a * b
if __name__ == '__main__':
    ellipse1_area = area_of_ellipse(A_SEMI_MAJOR, B_SEMI_MINOR)
    ellipse2_area = area_of_ellipse(C_SEMI_MAJOR, D_SEMI_MINOR)
    total_area = ellipse1_area + ellipse2_area
    print(total_area)