import math
import time

def calculate_rectangle_area(w, h):
    return w * h

def calculate_circle_area(r):
    return math.pi * r ** 2

def benchmark_shapes(num_items, widths, heights, radii):
    start_rect = time.perf_counter()
    rect_areas = []
    for i in range(num_items):
        rect_areas.append(calculate_rectangle_area(widths[i], heights[i]))
    end_rect = time.perf_counter()
    rect_time = end_rect - start_rect

    start_circle = time.perf_counter()
    circle_areas = []
    for i in range(num_items):
        circle_areas.append(calculate_circle_area(radii[i]))
    end_circle = time.perf_counter()
    circle_time = end_circle - start_circle

    total_rect_area = sum(rect_areas)
    total_circle_area = sum(circle_areas)
    
    return {
        "rectangle_time": rect_time,
        "circle_time": circle_time,
        "total_rectangle_area": total_rect_area,
        "total_circle_area": total_circle_area
    }

if __name__ == '__main__':
    num_items = 10000
    widths = [10.0] * num_items
    heights = [20.0] * num_items
    radii = [5.0] * num_items
    
    results = benchmark_shapes(num_items, widths, heights, radii)
    
    print(results["rectangle_time"])
    print(results["circle_time"])
    print(results["total_rectangle_area"])
    print(results["total_circle_area"])