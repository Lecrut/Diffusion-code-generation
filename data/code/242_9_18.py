import math

def compare_areas():
    semicircle_area = 0.5 * math.pi * (4 ** 2)
    rectangle_area = 6 * 3
    return semicircle_area, rectangle_area

if __name__ == '__main__':
    semicircle, rectangle = compare_areas()
    print(f"Semicircle area: {semicircle:.10f}")
    print(f"Rectangle area: {rectangle:.10f}")