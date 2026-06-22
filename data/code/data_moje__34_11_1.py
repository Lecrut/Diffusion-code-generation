import math

def compute_cylinder_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    return (lateral_area, total_area)
if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral, total = compute_cylinder_areas(radius, height)
    print(f'Lateral Surface Area: {lateral:.2f}')
    print(f'Total Surface Area: {total:.2f}')