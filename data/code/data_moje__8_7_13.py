import time
import math

def calculate_rectangle_areas(sides):
    return [s[0] * s[1] for s in sides]

def calculate_circle_areas(radii):
    return [math.pi * r * r for r in radii]

def benchmark_function(func, data, iterations=1):
    start = time.perf_counter()
    for _ in range(iterations):
        func(data)
    end = time.perf_counter()
    return end - start

def main():
    rect_sides = [(i, i + 1) for i in range(10000)]
    circle_radii = [i * 0.1 for i in range(10000)]

    rect_time = benchmark_function(calculate_rectangle_areas, rect_sides)
    circle_time = benchmark_function(calculate_circle_areas, circle_radii)

    rect_results = calculate_rectangle_areas(rect_sides)
    circle_results = calculate_circle_areas(circle_radii)

    print(f"Rectangle Area (first): {rect_results[0]}")
    print(f"Rectangle Total Time: {rect_time:.6f}")
    print(f"Circle Area (first): {circle_results[0]}")
    print(f"Circle Total Time: {circle_time:.6f}")

if __name__ == '__main__':
    main()