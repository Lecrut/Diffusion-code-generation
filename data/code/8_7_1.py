import math
import time

def calculate_rectangle_areas(count, width, height):
    results = [width * height for _ in range(count)]
    return results

def calculate_circle_areas(count, radius):
    results = [math.pi * radius * radius for _ in range(count)]
    return results

def benchmark(func, count, *args):
    start = time.perf_counter()
    func(count, *args)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    n = 10000
    w = 10.0
    h = 5.0
    r = 3.0

    rect_time = benchmark(calculate_rectangle_areas, n, w, h)
    circ_time = benchmark(calculate_circle_areas, n, r)

    print(f"Rectangle Area Calculation Time: {rect_time:.6f} seconds")
    print(f"Circle Area Calculation Time: {circ_time:.6f} seconds")
    print(f"Ratio (Rect/Circle): {rect_time / circ_time:.4f}")
    sample_rect_area = calculate_rectangle_areas(1, w, h)[0]
    sample_circle_area = calculate_circle_areas(1, r)[0]
    print(f"Sample Rectangle Area: {sample_rect_area}")
    print(f"Sample Circle Area: {sample_circle_area}")