import time
import math

def calculate_rectangle_area(widths, heights):
    """Calculate total area of rectangles using basic multiplication."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_areas(radii):
    """Calculate total area of circles using pi*r^2 formula."""
    return math.pi * (r**2 for r in radii)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    
    num_rectangles = 10_000
    max_width = 5.0
    max_height = 3.0
    
    rectangles_data = []
    
    for i in range(num_rectangles):
        w = (i % 20) * (max_width / 20) + 0.1
        h = ((i // 20) % 5) * (max_height / 5) + 0.1
        rectangles_data.append((w, h))

    num_circles = 10_000
    
    circles_data = []
    
    for i in range(num_circles):
        r = ((i // 30)) ** 0.2 * (max_width / 5) + 0.1
        circles_data.append(r)

    # Benchmark rectangles
    start_rect = time.perf_counter()
    rect_area_total = calculate_rectangle_area([w for w, h in rectangles_data], [h for w, h in rectangles_data])
    end_rect = time.perf_counter()
    
    print(f"Rectangle Area Calculation: {rect_area_total:.4f}")

    # Benchmark circles (using a generator expression inside sum)
    start_circle = time.perf_counter()
    circle_areas_list = [math.pi * r**2 for r in circles_data]
    circle_area_total = sum(circle_areas_list)
    end_circle = time.perf_counter()

    print(f"Circle Area Calculation: {circle_area_total:.4f}")

    # Output execution times and comparison
    exec_time_rect = end_rect - start_rect
    exec_time_circle = end_circle - start_circle
    
    print(f"\nExecution Time Comparison:")
    print(f"Rectangles (10,000):   {exec_time_rect*1e3:.4f} ms")
    print(f"Circles  (10,000):     {exec_time_circle*1e3:.4f} ms")

    if exec_time_rect > 0 and exec_time_circle > 0:
        ratio = exec_time_circle / exec_time_rect
        print(f"Performance Ratio (Circle/Rect): {ratio:.2f}")