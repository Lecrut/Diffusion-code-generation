import math
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_parallelogram_area(base, height):
    return base * height
if __name__ == '__main__':
    triangle_base = 10.0
    triangle_height = 5.0
    parallelogram_base = 8.0
    parallelogram_height = 6.0
    triangle_area = calculate_triangle_area(triangle_base, triangle_height)
    parallelogram_area = calculate_parallelogram_area(parallelogram_base, parallelogram_height)
    print(f"Triangle Base: {triangle_base}, Height: {triangle_height}")
    print(f"Area of the Triangle: {triangle_area}")
    print("-" * 20)
    print(f"Parallelogram Base: {parallelogram_base}, Height: {parallelogram_height}")
    print(f"Area of the Parallelogram: {parallelogram_area}")