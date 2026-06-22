import math

def compute_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    b1 = 10.0
    h1 = 5.0
    area1 = compute_triangle_area(b1, h1)
    print(area1)

    b2 = 7.5
    h2 = 3.2
    area2 = compute_triangle_area(b2, h2)
    print(area2)

    b3 = 0
    h3 = 100
    area3 = compute_triangle_area(b3, h3)
    print(area3)